#!!THIS CODE WAS WRITTEN BY {ENG.YAZAN_TAHA}&{ENG.LAILA_SAIFAN}&{ENG.ASHED_AL3KESH}    
import time
import requests
import os

# Configuration
TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = "TELEGRAM_CHAT_ID"
LOG_FILE = "/var/log/secure"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def monitor_log():
    # Open the log file and move to the end
    if not os.path.exists(LOG_FILE):
        print(f"Error: {LOG_FILE} not found.")
        return

    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        print("Sentinel is watching for unauthorized access...")
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            
            # Detect failed SSH login attempts
            if "Failed password" in line:
                try:
                    # Extract IP address from the log line
                    ip_start = line.find("from") + 5
                    ip_end = line.find("port")
                    ip_address = line[ip_start:ip_end].strip()
                    
                    hostname = os.uname()[1]
                    msg = f"🚨 Alert: Failed Login Attempt!\nIP: {ip_address}\nHost: {hostname}\nLog: {line.strip()}"
                    send_telegram_msg(msg)
                except Exception as e:
                    print(f"Parsing error: {e}")

if __name__ == "__main__":
    send_telegram_msg("✅ Sentinel Security Service Started Successfully!")
    monitor_log()
