# Linux Security Sentinel 🛡️

A lightweight Python-based Intrusion Detection System (IDS) that monitors system logs for failed SSH login attempts and sends real-time alerts via Telegram.

## Features
- **Real-time Monitoring:** Tracks `/var/log/secure` for authentication failures.
- **Instant Alerts:** Sends detailed notifications (IP, Hostname, Timestamp) to a Telegram Bot.
- **Systemd Integration:** Runs as a background service with auto-restart capabilities.
- **Lightweight:** Minimal CPU and RAM usage.

## Files
- `monitor.py`: The core Python engine.
- `sentinel.service`: Systemd unit file for service management.

## Setup
1. Clone the repo.
2. Update `TOKEN` and `CHAT_ID` in `monitor.py`.
3. Copy `sentinel.service` to `/etc/systemd/system/`.
4. Run `sudo systemctl enable --now sentinel.service`.

**Created by: ENG.YAZAN_TAHA & ENG.LAILA_SAIFAN & ENG.RASHED_AL3KESH **
