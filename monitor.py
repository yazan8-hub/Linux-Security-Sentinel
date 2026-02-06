import time
import requests
import os

# Configuration
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SSH_LOG = "/var/log/secure"
USB_LOG = "/var/log/messages"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error sending message: {e}")

def monitor_logs():
    # Open both log files
    f_ssh = open(SSH_LOG, "r")
    f_usb = open(USB_LOG, "r")
    
    # Move to the end of files
    f_ssh.seek(0, os.SEEK_END)
    f_usb.seek(0, os.SEEK_END)
    
    print("Sentinel 2.0 is watching SSH & USB events...")
    
    while True:
        # Check SSH Logs
        ssh_line = f_ssh.readline()
        if ssh_line and "Failed password" in ssh_line:
            msg = f"🚨 SSH Alert: Failed Login Attempt!\nDetails: {ssh_line.strip()}"
            send_telegram_msg(msg)
            
        # Check USB Logs
        usb_line = f_usb.readline()
        if usb_line and "New USB device found" in usb_line:
            msg = f"🔌 USB Alert: New Device Detected!\nDetails: {usb_line.strip()}"
            send_telegram_msg(msg)
            
        time.sleep(0.5)

if __name__ == "__main__":
    send_telegram_msg("✅ Sentinel 2.0 Started: Monitoring SSH & USB")
    monitor_logs()
