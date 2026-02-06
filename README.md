# Linux Security Sentinel (v3.0 - ChatOps Edition) 🛡️

An advanced, modular Security Suite built with Python and Systemd. This project combines real-time system monitoring with an interactive **ChatOps** controller via Telegram, allowing for remote server auditing and management.



## 🚀 Key Features

### 1. Proactive Monitoring (Service: sentinel)
- **SSH Brute-Force Detection:** Monitors `/var/log/secure` for failed login attempts.
- **USB Intrusion Detection:** Detects new hardware connections (Mass Storage/HID) via kernel logs.
- **Real-time Alerts:** Instant Telegram notifications for any security event.

### 2. Interactive ChatOps (Service: sentinel-interactive)
- **Remote Commands:** Query your server directly from Telegram:
    - `/who` - See currently logged-in users.
    - `/status` - Check CPU, RAM, and Uptime.
    - `/sys_info` - Get Kernel and CPU architecture details.
    - `/logs` - View the last 10 failed SSH attempts.
    - `/net` - List active network listening ports.

## 🛠️ Technical Stack
- **Language:** Python 3.12
- **OS:** RHEL 10 / Fedora (SELinux Compatible)
- **Service Manager:** Systemd (Dual-service architecture)
- **API:** python-telegram-bot (Telebot)

## 📂 Project Structure
- `monitor.py`: The background monitoring engine.
- `commands.py`: The interactive command controller.
- `sentinel.service`: Systemd unit for monitoring.
- `sentinel-interactive.service`: Systemd unit for the bot controller.
- `.env`: Encrypted-style environment variables for security.

## 🔧 Installation & Deployment
# 1. Clone the repository
git clone https://github.com/yazan8-hub/Linux-Security-Sentinel.git
cd Linux-Security-Sentinel

# 2. Configure Environment (Create .env and add your credentials)
echo "TELEGRAM_TOKEN=your_token_here" > .env
echo "TELEGRAM_CHAT_ID=your_id_here" >> .env

# 3. System Setup & SELinux Contexts
sudo pip install pyTelegramBotAPI
sudo chcon -t bin_t monitor.py commands.py
sudo chcon -t etc_t .env

# 4. Activate Services
sudo cp *.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now sentinel.service
sudo systemctl enable --now sentinel-interactive.service

**Created by: ENG.YAZAN_TAHA & ENG.LAILA_SAIFAN & ENG.RASHED_AL3KESH **
