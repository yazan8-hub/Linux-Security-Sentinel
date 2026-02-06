# Linux Security Sentinel (v2.0) 🛡️

A proactive, lightweight Intrusion Detection System (IDS) developed in Python. It monitors critical system logs to detect unauthorized access attempts and hardware intrusions, providing real-time alerts via Telegram.



## 🚀 Features
- **SSH Brute-Force Detection:** Monitors `/var/log/secure` for failed authentication attempts.
- **USB Hardware Monitoring:** Tracks `/var/log/messages` to detect new hardware connections (Mass Storage, HID, etc.).
- **Real-time Alerts:** Instant notifications via Telegram Bot API with detailed metadata (IP, Hostname, Device Info).
- **Systemd Integration:** Runs as a persistent background service with auto-restart capability.
- **SELinux Compatible:** Optimized for Fedora/Red Hat environments with proper security context handling.

## 🛠️ Technical Stack
- **Language:** Python 3.x
- **OS:** Linux (Tested on Fedora/Red Hat)
- **Service Manager:** Systemd
- **Messaging:** Telegram Bot API

## 📂 File Structure
- `monitor.py`: The core detection engine.
- `sentinel.service`: Systemd unit file for service management.
- `.env`: (Hidden) Stores sensitive credentials (API Token & Chat ID).
- `.gitignore`: Prevents sensitive configuration leaks to GitHub.

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yazan8-hub/Linux-Security-Sentinel.git](https://github.com/yazan8-hub/Linux-Security-Sentinel.git)
   cd Linux-Security-Sentinel

**Created by: ENG.YAZAN_TAHA & ENG.LAILA_SAIFAN & ENG.RASHED_AL3KESH **
