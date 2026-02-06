import telebot
import os
import subprocess
from datetime import datetime

# Configuration
TOKEN = os.getenv("TELEGRAM_TOKEN")
MY_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = telebot.TeleBot(TOKEN)

def is_authorized(message):
    return str(message.chat.id) == str(MY_CHAT_ID)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if is_authorized(message):
        help_text = (
            "🛡️ Sentinel Command Center\n\n"
            "/who - Current logged in users\n"
            "/status - CPU & Memory usage\n"
            "/screenshot - Take a real-time screenshot\n"
            "/logs - Last 10 SSH auth failures\n"
            "/net - Active network connections\n"
            "/sys_info - System hardware information\n"
        )
        bot.reply_to(message, help_text,)

@bot.message_handler(commands=['who'])
def cmd_who(message):
    if is_authorized(message):
        res = subprocess.getoutput('who')
        bot.reply_to(message, f"👥 **Users:**\n`{res if res else 'No users'}`", parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def cmd_status(message):
    if is_authorized(message):
        uptime = subprocess.getoutput('uptime -p')
        mem = subprocess.getoutput("free -h | awk 'NR==2{print $3 \"/\" $2}'")
        cpu = subprocess.getoutput("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'")
        bot.reply_to(
            message,
            f"📊 **Status:**\n⏱ {uptime}\n💾 RAM: {mem}\n🔥 CPU Load: {cpu}%",
            parse_mode='Markdown'
        )

@bot.message_handler(commands=['screenshot'])
def cmd_screenshot(message):
    if is_authorized(message):
        photo_path = "/tmp/screen.png"
        try:
            # Use DISPLAY=:0 to capture the main GUI session
            subprocess.run(["scrot", "-z", photo_path], env={"DISPLAY": ":0"})
            with open(photo_path, 'rb') as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=f"📸 Captured at {datetime.now().strftime('%H:%M:%S')}"
                )
            os.remove(photo_path)
        except Exception as e:
            bot.reply_to(
                message,
                f"❌ Screenshot failed: {e}\n(Make sure you are logged into a GUI session)"
            )

@bot.message_handler(commands=['logs'])
def cmd_logs(message):
    if is_authorized(message):
        # Fetch last 10 SSH authentication failures
        res = subprocess.getoutput(
            'sudo tail -n 50 /var/log/secure | grep "Failed password" | tail -n 10'
        )
        bot.reply_to(
            message,
            f"🚨 **Last SSH Failures:**\n`{res if res else 'No failures found'}`",
            parse_mode='Markdown'
        )

@bot.message_handler(commands=['net'])
def cmd_net(message):
    if is_authorized(message):
        # Show currently listening ports
        res = subprocess.getoutput('ss -tulpn | grep LISTEN | head -n 15')
        bot.reply_to(
            message,
            f"🌐 **Open Ports:**\n`{res}`",
            parse_mode='Markdown'
        )

@bot.message_handler(commands=['sys_info'])
def cmd_sys_info(message):
    if is_authorized(message):
        try:
            # Get CPU model
            cpu_model = subprocess.getoutput(
                "lscpu | grep 'Model name' | cut -d: -f2"
            ).strip()
            # Get number of CPU cores
            cpu_cores = subprocess.getoutput("nproc")
            # Try to get CPU temperature (may not work on VMs)
            temp = subprocess.getoutput(
                "sensors | grep 'Core 0' | awk '{print $3}'"
            )
            if not temp:
                temp = "N/A (Virtual Machine)"

            info_text = (
                f"🖥️ **System Architecture:**\n"
                f"🔹 **CPU:** {cpu_model}\n"
                f"🔹 **Cores:** {cpu_cores}\n"
                f"🔹 **Temp:** {temp}\n"
                f"🔹 **Kernel:** {subprocess.getoutput('uname -r')}"
            )
            bot.reply_to(message, info_text, parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"❌ Info failed: {e}")

print("🚀 Sentinel Interactive Suite is running...")
bot.polling()

