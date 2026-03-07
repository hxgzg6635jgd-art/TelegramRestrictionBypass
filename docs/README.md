<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0a0f,30:0d1117,60:161b22,100:1a1f2e&height=240&section=header&text=⚡%20TelegramRestrictionBypass&fontSize=42&fontColor=58a6ff&fontAlignY=42&animation=twinkling&desc=Production-grade%20%7C%20Multi-Bot%20Worker%20Pool%20%7C%20Auto-Resume%20%7C%20Live%20Dashboard&descAlignY=62&descSize=14&descColor=8b949e" width="100%"/>

</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python_3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pyrofork](https://img.shields.io/badge/Pyrofork-MTProto-FF6B35?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/KurimuzonAkuma/pyrogram)
[![TgCrypto](https://img.shields.io/badge/TgCrypto-Accelerated-00d4aa?style=for-the-badge)](https://github.com/pyrogram/tgcrypto)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square&logo=statuspage&logoColor=white)
&nbsp;
![Multi-Bot](https://img.shields.io/badge/Multi--Bot_Pool-Unlimited_Workers-a78bfa?style=flat-square)
&nbsp;
![Batch](https://img.shields.io/badge/Batch_DL-200_msgs%2Fchunk-f59e0b?style=flat-square)
&nbsp;
![Auto Resume](https://img.shields.io/badge/Auto_Resume-On_Crash-06b6d4?style=flat-square)
&nbsp;
![Modes](https://img.shields.io/badge/Modes-BOT_%2B_USER-ec4899?style=flat-square)

</div>

<br/>

<div align="center">

```
╔═══════════════════════════════════════════════════════════════════╗
║  Download & re-upload restricted Telegram content at production   ║
║  scale — with a live admin dashboard, round-robin worker pools,   ║
║  crash-safe auto-resume, and dual BOT/USER download modes.        ║
╚═══════════════════════════════════════════════════════════════════╝
```

**Developed by [@Paidguy](https://github.com/Paidguy)**
&nbsp;•&nbsp;
Enhanced from [RestrictedContentDL](https://github.com/bisnuray/RestrictedContentDL) by [@bisnuray](https://github.com/bisnuray)

</div>

---

## 🚀 Quick Start

**New to this project? Start here!**

👉 **[Complete Setup Guide (SETUP.md)](SETUP.md)** 👈

A step-by-step walkthrough covering:
- ✅ Installing Python and dependencies
- ✅ Getting Telegram API credentials
- ✅ Creating your bot with BotFather
- ✅ Configuring and running the bot
- ✅ Troubleshooting common issues

**Want a super quick checklist?** See [QUICKSTART.md](QUICKSTART.md) for a condensed version.

**Experienced users:** Jump to [Installation Methods](#-installation-methods) below.

---

## 📑 Table of Contents

<table>
<tr>
<td valign="top" width="50%">

**Setup**
- [🚀 Quick Start & Setup Guide](SETUP.md)
- [✨ Features at a Glance](#-features-at-a-glance)
- [🏗️ Architecture & How It Works](#️-architecture--how-it-works)
- [🔑 Prerequisites Checklist](#-prerequisites-checklist)
- [🔐 Getting Your Credentials](#-getting-your-credentials)
  - [API ID & API Hash](#1-api-id--api-hash)
  - [Bot Tokens](#2-bot-tokens)
  - [Session String](#3-session-string)
- [⚙️ Configuration Reference](#️-configuration-reference)

</td>
<td valign="top" width="50%">

**Deployment**
- [📦 Installation Methods](#-installation-methods)
  - [Local / VPS](#method-1--local--vps)
  - [Docker Compose](#method-2--docker-compose)
  - [AWS with Systemd](#method-3--aws--cloud-with-systemd)
- [🚀 First Run Walkthrough](#-first-run--setup-walkthrough)
- [🤖 Commands Reference](#-commands-reference)
- [📊 Admin Dashboard Guide](#-admin-dashboard-guide)
- [🔄 Multi-Bot Worker Pool](#-multi-bot-worker-pool)
- [📁 Project Structure](#-project-structure--runtime-files)
- [🐛 Bug Fixes in This Release](#-bug-fixes-in-this-release)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [⚠️ Legal Disclaimer](#️-legal-disclaimer)

</td>
</tr>
</table>

---

## ✨ Features at a Glance

<table>
<tr>
<td width="50%" valign="top">

### ⚡ Core Engine
| Feature | Details |
|---|---|
| **Clone Channel** | `/clone <link>` — entire channel with one command (NEW!) |
| **Single Download** | `/dl <link>` — any one Telegram message |
| **Batch Download** | `/bdl <start> <end>` — thousands at once |
| **Media Groups** | Albums re-uploaded together, intact |
| **BOT Mode** | Uses bot token(s) to fetch content |
| **USER Mode** | Uses your account session to access restricted content |
| **Auto-Resume** | Interrupted batches restart automatically on reboot |
| **FloodWait Guard** | Exponential backoff, auto-retry up to 5× |

</td>
<td width="50%" valign="top">

### 🛡️ Production Features
| Feature | Details |
|---|---|
| **Multi-Bot Pool** | Unlimited worker bots, round-robin distribution |
| **Live Dashboard** | RAM, storage, uptime, active downloads — live |
| **Dump Channel** | Forward all output to a target Telegram channel |
| **Source History** | Track all cloned channels automatically |
| **User Auth** | Restrict to specific Telegram user IDs |
| **TgCrypto** | C-level crypto for maximum transfer speed |
| **Auto Cleanup** | Temp files removed on startup and after each upload |
| **Persistent Settings** | All config survives restarts via local JSON |

</td>
</tr>
</table>

---

## 🏗️ Architecture & How It Works

### System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      USER / ADMIN                               │
│                  (your Telegram account)                        │
└─────────────────────┬───────────────────────────────────────────┘
                      │  /dl or /bdl command
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MAIN BOT (control plane)                     │
│   • Receives commands      • Manages dashboard & settings       │
│   • Authorizes users       • Distributes work to workers        │
└──────┬──────────────────────────────────┬───────────────────────┘
       │                                  │
       ▼                                  ▼
┌──────────────┐                 ┌────────────────────────────────┐
│  USER CLIENT │                 │     WORKER BOT POOL            │
│  (session    │                 │  ┌─────────┐  ┌─────────┐     │
│   string)    │   round-robin   │  │ Worker1 │  │ Worker2 │ ··· │
│              │◄── selection ──►│  └─────────┘  └─────────┘     │
│ USER Mode ✓  │                 │  BOT Mode ✓                    │
└──────┬───────┘                 └────────────┬───────────────────┘
       │                                      │
       └──────────────┬───────────────────────┘
                      │  fetch message from Telegram
                      ▼
             ┌────────────────┐
             │  downloads/    │   (organized by message ID)
             │  temp storage  │
             └───────┬────────┘
                     │  upload
                     ▼
        ┌────────────────────────┐
        │  DESTINATION           │
        │  ┌──────────────────┐  │
        │  │  Dump Channel    │  │  ◄── if configured
        │  └──────────────────┘  │
        │  ┌──────────────────┐  │
        │  │  Back to User    │  │  ◄── default
        │  └──────────────────┘  │
        └────────────────────────┘
                     │
                     ▼
           🗑️ Temp file auto-deleted
```

### Download Modes Explained

| Mode | How it fetches | When to use |
|---|---|---|
| **BOT Mode** (default) | Worker bot tokens via Telegram Bot API | Public channels & content your bot can access |
| **USER Mode** | Your personal Telegram account session | Private/restricted channels bots can't see |

> You can **toggle between modes at runtime** from the dashboard — no restart needed.

### Batch Processing Flow

```
/bdl https://t.me/channel/100  https://t.me/channel/5000

 Range: msg 100 → 5000  (4,900 messages)
 Chunk size: 200 messages per API call
 ──────────────────────────────────────────────────────────
 Chunk 1:  100–299   → fetch 200 IDs → filter → parallel download → upload
 Chunk 2:  300–499   → fetch 200 IDs → filter → parallel download → upload
 ...
 Chunk 25: 4900–5000 → fetch 100 IDs → filter → parallel download → upload

 Progress saved after every message → crash-safe auto-resume ✓
 Media groups (albums) detected and sent together ✓
 Empty / deleted messages automatically skipped ✓
```

---

## 🔑 Prerequisites Checklist

```
✅  Python 3.11 or higher installed
✅  Git installed
✅  500 MB+ free disk space on your server
✅  Stable internet connection (low-latency to Telegram DCs preferred)
✅  Telegram API credentials (API_ID + API_HASH) from my.telegram.org
✅  At least one Telegram Bot Token from @BotFather
✅  (Optional) A Telegram user account for User Mode
✅  (Optional) Docker + Docker Compose for containerized deployment
```

> 💡 You can run **without a Session String** in BOT-only mode. User Mode is only needed to access content that bots cannot reach — e.g. private channels or subscriber-only content.

---

## 🔐 Getting Your Credentials

### 1. API ID & API Hash

These credentials identify your Telegram *application*. Every app using the Telegram API needs them.

**Steps:**

1. Open [https://my.telegram.org](https://my.telegram.org) in your browser
2. Enter your phone number (with country code, e.g. `+12025551234`) and click **Send Code**
3. Enter the OTP Telegram sends to your account
4. Click **"API development tools"**
5. Fill out the form (App title, short name, and description can be anything)
6. Click **Create application**
7. Copy the values shown for **`App api_id`** (integer) and **`App api_hash`** (hex string)

```env
API_ID=12345678
API_HASH=a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4
```

> ⚠️ **These are tied to your personal Telegram account.** Never share them. If compromised, revoke them at my.telegram.org immediately.

---

### 2. Bot Tokens

Each bot token = one upload/download worker. More tokens = more throughput.

**Creating your main bot:**

1. Open Telegram → search **[@BotFather](https://t.me/BotFather)**
2. Send `/newbot`
3. Enter a display name (e.g. `My Downloader`)
4. Enter a unique username ending in `bot` (e.g. `mydownloaderbot`)
5. BotFather replies with your token:
   ```
   1234567890:ABCdefGhIjKlMnOpQrStUvWxYz-abc123
   ```

**Adding worker bots (optional but recommended for heavy use):**

Repeat the above for each additional bot. Comma-separate all tokens in `config.env`:

```env
# Single bot:
BOT_TOKENS=1234567890:ABCdef...

# Multiple bots — first is main (control), rest become workers:
BOT_TOKENS=1111111:AAA...,2222222:BBB...,3333333:CCC...
```

> 💡 Each extra worker bot adds one more parallel upload slot. For batch downloads of thousands of files, 3–5 bots dramatically improves throughput.

---

### 3. Session String

A session string encodes your Telegram user account login. Required for USER Mode.

**Self-hosted generator (most secure — recommended):**

Create `gen_session.py` in the project root:

```python
import asyncio
from pyrogram import Client

API_ID   = 12345678                       # ← your API_ID
API_HASH = "your_api_hash_here"           # ← your API_HASH

async def main():
    async with Client("session_gen", api_id=API_ID, api_hash=API_HASH) as app:
        session = await app.export_session_string()
        print("\n" + "=" * 60)
        print("YOUR SESSION STRING:")
        print("=" * 60)
        print(session)
        print("=" * 60 + "\n")

asyncio.run(main())
```

Run it:

```bash
python3 gen_session.py
```

- Enter your phone number when prompted
- Enter the OTP Telegram sends you
- Enter your 2FA password if you have one enabled
- Copy the long string printed between the `===` lines

```env
SESSION_STRING=BQA...very_long_string...
```

**After generating:**
- Delete `session_gen.session` — the string is what matters
- Delete `gen_session.py` for security
- Store the string in `config.env` only — never commit it to Git

> ⚠️ The session string grants **full access to your Telegram account**. Treat it like your password.

---

## ⚙️ Configuration Reference

Edit `config.env` — the single source of truth for all settings:

```env
# ════════════════════════════════════════════════════════════
#  🔑  TELEGRAM API CREDENTIALS
#  Get these from: https://my.telegram.org
# ════════════════════════════════════════════════════════════

API_ID=12345678
API_HASH=a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4


# ════════════════════════════════════════════════════════════
#  🤖  BOT TOKENS
#  First token = main (control) bot
#  Additional tokens = worker bots (comma-separated, no spaces)
# ════════════════════════════════════════════════════════════

BOT_TOKENS=1111111111:AAAbbbCCC...,2222222222:DDDeee...


# ════════════════════════════════════════════════════════════
#  🔐  USER SESSION STRING
#  Required only for USER Mode (accessing restricted channels)
#  Leave empty to run in BOT-only mode
# ════════════════════════════════════════════════════════════

SESSION_STRING=BQAx...your_session_string_here...


# ════════════════════════════════════════════════════════════
#  ⚡  PERFORMANCE TUNING
# ════════════════════════════════════════════════════════════

# Max files downloading simultaneously (default: 5)
# Reduce to 2–3 if you frequently hit FloodWait errors
# Increase to 6–8 if you have many worker bots and a fast server
MAX_CONCURRENT_DOWNLOADS=5

# Seconds to pause between batch API chunks (default: 2)
# Increase to 5–10 on slow servers or if rate-limited
FLOOD_WAIT_DELAY=2

# Message IDs fetched per Telegram API call (default: 200)
# Reduce to 50–100 if you get timeout errors on slow connections
BATCH_SIZE=200
```

### Full Variable Reference

| Variable | Type | Default | Description |
|---|---|---|---|
| `API_ID` | Integer | **required** | Telegram app ID from my.telegram.org |
| `API_HASH` | String | **required** | Telegram app hash from my.telegram.org |
| `BOT_TOKENS` | String (CSV) | **required** | One or more bot tokens, comma-separated. First = main bot. |
| `SESSION_STRING` | String | `""` | User account session. Empty = BOT-only mode. |
| `MAX_CONCURRENT_DOWNLOADS` | Integer | `5` | Max files downloading simultaneously |
| `FLOOD_WAIT_DELAY` | Integer | `2` | Seconds of pause between batch chunks |
| `BATCH_SIZE` | Integer | `200` | Message IDs fetched per Telegram API call |

---

## 📦 Installation Methods

| Method | Best For | Difficulty |
|---|---|---|
| [Local / VPS](#method-1--local--vps) | Getting started, development | ⭐ Easy |
| [Docker Compose](#method-2--docker-compose) | Production, clean environments | ⭐⭐ Medium |
| [AWS + Systemd](#method-3--aws--cloud-with-systemd) | Always-on cloud servers | ⭐⭐⭐ Involved |

---

### Method 1 — Local / VPS

Works on Ubuntu, Debian, CentOS, macOS, and WSL2.

**Step 1 — Install Python 3.11+**

```bash
# Ubuntu / Debian
sudo apt update && sudo apt install python3.11 python3.11-venv python3-pip git -y

# Verify
python3 --version   # must be 3.11.x or higher
```

**Step 2 — Clone the repository**

```bash
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass
```

**Step 3 — Create a virtual environment**

```bash
python3.11 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# Confirm you're inside the venv:
which python    # should show ...venv/bin/python
```

**Step 4 — Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

| Package | Purpose |
|---|---|
| `Pyrofork` | Maintained Pyrogram fork — Telegram MTProto client |
| `TgCrypto` | C-extension accelerating Telegram's AES-256-IGE crypto |
| `Pyleaves` | Progress bar display for upload/download |
| `python-dotenv` | Loads `config.env` into the environment |
| `psutil` | System metrics (RAM %, disk usage) for dashboard |
| `Pillow` | Image processing for video thumbnails |

**Step 5 — Configure credentials**

```bash
nano config.env    # fill in API_ID, API_HASH, BOT_TOKENS, SESSION_STRING
```

**Step 6 — Run the bot**

```bash
python3 main.py
```

You should see startup logs:
```
[DD-Mon-YY HH:MM:SS AM] - INFO - Starting User Session...
[DD-Mon-YY HH:MM:SS AM] - INFO - Initializing Bots...
[DD-Mon-YY HH:MM:SS AM] - INFO - System Starting...
```

Open Telegram, message your bot, and send `/start`.

**Keep it alive after SSH logout:**

```bash
screen -S tgbot        # start a named screen session
python3 main.py        # run inside it
# Ctrl+A then D to detach (bot keeps running)
# screen -r tgbot to reattach later
```

---

### Method 2 — Docker Compose

Docker ensures a clean, reproducible environment with zero dependency conflicts.

**Install Docker:**

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker

sudo apt install docker-compose-plugin -y

# Verify
docker --version
docker compose version
```

**Clone and configure:**

```bash
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass
nano config.env    # fill in your credentials
```

**Review `docker-compose.yml`:**

```yaml
services:
  media_bot:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - TZ=Asia/Dhaka       # ← change to your timezone
    restart: always          # auto-restart on crash or system reboot
    network_mode: "host"     # critical for Telegram connectivity
    volumes:
      - .:/app               # live-mounts project dir (no rebuild needed for config changes)
```

> 📝 Find your timezone string at [Wikipedia — tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

**Build and start:**

```bash
docker compose up -d --build   # first-time build (~3 minutes)
docker compose logs -f          # follow live logs
```

**Common Docker commands:**

```bash
docker compose ps                    # is it running?
docker compose restart               # restart the bot
docker compose down                  # stop and remove container
docker compose up -d --build         # rebuild after code changes
docker compose exec media_bot bash   # shell inside the container
```

**Update the bot:**

```bash
git pull && docker compose up -d --build
```

---

### Method 3 — AWS / Cloud with Systemd

Sets up the bot as a proper OS service: starts on boot, restarts on failure.

**Recommended instance specs:**
- **CPU:** 1 vCPU minimum, 2+ for heavy batch
- **RAM:** 1 GB minimum, 2+ recommended
- **Storage:** 20 GB minimum
- **OS:** Ubuntu 22.04 LTS

**Step 1 — Connect and prepare**

```bash
ssh -i your-key.pem ubuntu@YOUR_SERVER_IP
sudo apt update && sudo apt upgrade -y
sudo apt install python3.11 python3.11-venv python3-pip git -y
```

**Step 2 — Clone and set up**

```bash
cd /home/ubuntu
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass

python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
nano config.env    # fill in credentials
```

**Step 3 — Create the systemd service**

```bash
sudo nano /etc/systemd/system/tgbypass.service
```

Paste the following:

```ini
[Unit]
Description=Telegram Restriction Bypass Bot
Documentation=https://github.com/Paidguy/TelegramRestrictionBypass
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/TelegramRestrictionBypass
ExecStart=/home/ubuntu/TelegramRestrictionBypass/venv/bin/python3 main.py
Restart=always
RestartSec=15
StartLimitInterval=200
StartLimitBurst=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=tgbypass

[Install]
WantedBy=multi-user.target
```

**Step 4 — Enable and start**

```bash
sudo systemctl daemon-reload
sudo systemctl enable tgbypass   # start on boot
sudo systemctl start tgbypass    # start now
sudo systemctl status tgbypass   # verify running
```

**Step 5 — Monitor**

```bash
sudo journalctl -u tgbypass -f          # live log stream
sudo journalctl -u tgbypass -n 100      # last 100 lines
sudo systemctl restart tgbypass         # restart after config change
```

**Updating:**

```bash
cd /home/ubuntu/TelegramRestrictionBypass
git pull
source venv/bin/activate && pip install -r requirements.txt
sudo systemctl restart tgbypass
```

> 💡 **AWS-specific fix — ConnectionResetError / disconnections:**
>
> ```bash
> # Disable IPv6 immediately
> sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
> sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
>
> # Make it permanent
> echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
> echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
> sudo sysctl -p && sudo systemctl restart tgbypass
> ```

---

## 🚀 First Run & Setup Walkthrough

Follow these steps **in order** after your first startup.

### Step 1 — Claim Ownership

Send `/start` to your bot in **private chat**. The first user to do this becomes the permanent **owner** — their Telegram user ID is written to `downloads/owner_id.txt`.

> 🔒 To reassign ownership: stop the bot, delete `downloads/owner_id.txt`, restart, then `/start` again.

---

### Step 2 — Read the Dashboard

```
🤖 Restricted Content Downloader
━━━━━━━━━━━━━━━━━━━━━
⚡ Active DLs: 0 | Tasks: 0
🤖 Worker Bots: 1 active
⏱ Uptime: 0h 0m 12s
💾 Storage: 18.4 GB free
🧠 RAM Load: 23%
━━━━━━━━━━━━━━━━━━━━━
📂 Destination: Private Chat
🛠 Current Mode: BOT
```

`Worker Bots: 1` — just your main bot running  
`Destination: Private Chat` — files come back directly to you  
`Current Mode: BOT` — using bot tokens to fetch (not user session)

---

### Step 3 — (Optional) Set a Dump Channel

Forward all downloads to a Telegram channel instead of your private chat:

1. Create or open a Telegram channel
2. **Channel Settings → Administrators → Add Administrator**
3. Add your bot with **"Post Messages"** permission
4. Done — the bot detects being promoted and saves the channel automatically

The dashboard updates to: `📂 Destination: Channel -1001234567890`

To clear it: delete `downloads/dump_target.txt` and restart.

---

### Step 4 — (Optional) Add Worker Bots

```
/connect 2222222222:BBBbbbCCC...
```

Each `/connect` adds one more worker. The dashboard shows the updated count: `🤖 Worker Bots: 2 active`

---

### Step 5 — (Optional) Authorize Other Users

```
/auth 987654321
```

Replace with the target user's Telegram numeric ID. They can find their own ID via [@userinfobot](https://t.me/userinfobot).

---

### Step 6 — (Optional) Switch to User Mode

In the dashboard, tap **"👤 User Mode"**. The bot confirms: `🛠 Current Mode: USER`

Switch back anytime by tapping **"🤖 Bot Mode"**.

> Requires a valid `SESSION_STRING` in `config.env`. If missing or expired, the bot logs a warning and stays in BOT mode.

---

## 🤖 Commands Reference

All commands are **private chat only**. Only the owner and authorized users can use them.

### Download Commands

| Command | Syntax | Description |
|---|---|---|
| `/clone` | `/clone https://t.me/channel/123` | **Clone entire channel automatically** — discovers boundaries and downloads from start to finish |
| `/dl` | `/dl https://t.me/channel/123` | Download a single Telegram message |
| `/bdl` | `/bdl https://t.me/channel/100 https://t.me/channel/500` | Batch download messages 100 → 500 |

**Supported link formats:**

```
# Public channel
https://t.me/channelname/123

# Private channel (numeric ID)
https://t.me/c/1234567890/123

# Forum/topic thread (topic 45, message 123)
https://t.me/c/1234567890/45/123
```

### Admin Commands

| Command | Syntax | Description |
|---|---|---|
| `/start` | `/start` | Open the live admin dashboard |
| `/connect` | `/connect <bot_token>` | Add a bot to the worker pool at runtime |
| `/join` | `/join <link_or_username>` | Join a chat as the user account (USER Mode only) |
| `/auth` | `/auth <user_id>` | Authorize a user (owner only) |
| `/logs` | `/logs` | Send `logs.txt` to your chat |
| `/clean` | `/clean` | Wipe all temp files from `downloads/` |

### Example Usage

```bash
# Clone an entire channel (automatic boundary detection)
/clone https://t.me/techcommunity/100

# Download one video
/dl https://t.me/techcommunity/4521

# Batch download 200 files from a private channel
/bdl https://t.me/c/1234567890/1 https://t.me/c/1234567890/200

# Add a second worker bot
/connect 9876543210:XYZ-abc123def456...

# Authorize a user
/auth 123456789

# Join a private group as your user account
/join https://t.me/+AbCdEfGhIjKl
```

### Batch Resume / Restart

When a batch is interrupted and you send `/bdl` again (without arguments), the bot offers:

```
⚠️ Found Batch!
Range: 100 - 5000

[ ▶️ Resume (847) ]   ← continue from message 847
[ 🔄 Start Over   ]   ← restart from message 100
[ ✖️ Cancel       ]   ← discard the saved batch state
```

---

## 📊 Admin Dashboard Guide

### Dashboard Layout

```
┌────────────────────────────────────────────┐
│  🤖 Restricted Content Downloader         │
│  ━━━━━━━━━━━━━━━━━━━━━                    │
│  ⚡ Active DLs: 2 | Tasks: 3              │
│  🤖 Worker Bots: 3 active                 │
│  ⏱ Uptime: 4h 23m 15s                   │
│  💾 Storage: 8.1 GB free                 │
│  🧠 RAM Load: 61%                         │
│  ━━━━━━━━━━━━━━━━━━━━━                    │
│  📂 Destination: Channel -10012345        │
│  🛠 Current Mode: BOT                     │
│                                            │
│  [ 🔄 Refresh ]  [ ⚙️ Settings ]          │
│  [ 🤖 Manage Bots ] [ 👤 User Mode ]      │
│  [ 📜 Logs ]  [ 🛑 STOP ALL ]             │
└────────────────────────────────────────────┘
```

| Button | What it does |
|---|---|
| **🔄 Refresh** | Pulls fresh stats and redraws the dashboard |
| **⚙️ Settings** | Opens speed / delay settings panel |
| **🤖 Manage Bots** | View, inspect, and remove worker bots |
| **👤 User Mode / 🤖 Bot Mode** | Toggle download mode (instant, no restart) |
| **📜 Logs** | Sends `logs.txt` to your chat for debugging |
| **🛑 STOP ALL** | Immediately cancels all in-progress tasks |

### Settings Panel

```
[ ⚡ Speed: 5x ]  [ ⏳ Delay: 2s ]
[ 🔙 Back ]
```

| Button | Toggles Between | Effect |
|---|---|---|
| **⚡ Speed** | `3x` ↔ `5x` | Changes `max_concurrent` simultaneous downloads |
| **⏳ Delay** | `0s` ↔ `2s` | Changes pause between batch API chunks |

### Bot Manager Panel

```
🤖 Bot Manager — Active Workers: 3

[ 🤖 MainBot (Main)  ]
[ 🤖 Worker2         ] [ 🗑 ]
[ 🤖 Worker3         ] [ 🗑 ]
[ 🔙 Back ]
```

- **Tap any bot name** to view its ID, username, role, and connection status
- **Tap 🗑** to remove a worker bot (main bot is protected and cannot be removed)
- Removed bots are also purged from `downloads/extra_bots.txt`

---

## 🔄 Smart Clone System

### Overview

The **Smart Clone System** is one of the most powerful features of TelegramRestrictionBypass. It allows you to clone entire Telegram channels with a single command — no need to manually find message IDs or configure ranges. Just paste any message link from the channel, and the bot automatically discovers the channel boundaries and downloads everything from start to finish.

### Key Features

<table>
<tr>
<td width="50%" valign="top">

#### 🎯 Automatic Discovery
- **Auto-detects** channel boundaries
- **Scans** to find the latest message
- **Determines** full range (1 → latest)
- **No manual setup** required

#### 🚀 Performance
- **Parallel downloads** with worker pools
- **Batch processing** in 200-message chunks
- **Direct forwarding** for unprotected content
- **Concurrent uploads** via multiple bots

</td>
<td width="50%" valign="top">

#### 🛡️ Reliability
- **Crash-safe** state persistence
- **Auto-resume** from interruption point
- **FloodWait handling** with backoff
- **Error recovery** and retry logic

#### 📊 Tracking
- **Source history** of cloned channels
- **Real-time progress** updates
- **Dashboard monitoring** of active clones
- **Completion notifications**

</td>
</tr>
</table>

### How Clone Works

#### Step-by-Step Process

1. **User sends command** — `/clone https://t.me/channel/123`
2. **Link parsing** — Bot extracts chat ID from the link
3. **Boundary scanning** — Bot fetches channel history to find latest message
4. **Range determination** — Sets start=1, end=latest_message_id
5. **State persistence** — Saves batch to `downloads/user_state.json`
6. **Batch processing** — Downloads in 200-message chunks
7. **Progress updates** — Reports every 200 messages
8. **Auto-resume** — Recovers from crashes automatically
9. **Completion** — Notifies when all messages downloaded

#### Technical Flow

```
/clone https://t.me/channel/500
          │
          ▼
Parse chat ID from link
          │
          ▼
Fetch chat_history(limit=1) → Get latest message ID (e.g., 5432)
          │
          ▼
Determine range: start=1, end=5432
          │
          ▼
Save state to downloads/user_state.json
          │
          ▼
run_batch_logic(1, 5432)
          │
          ├─► Chunk 1: Messages 1-200
          ├─► Chunk 2: Messages 201-400
          ├─► Chunk 3: Messages 401-600
          │   ...
          └─► Chunk 28: Messages 5401-5432
          │
          ▼
✅ Batch Complete! Total: 5,432 messages
```

### Usage Examples

#### Basic Clone

```bash
# Clone a public channel
/clone https://t.me/techcommunity/100

# What the bot does:
# 🔍 Scanning channel to find latest message...
# ✓ Found: Message 5,432 (latest)
# 📊 Range determined: 1 → 5,432
# 🚀 Batch Started (BOT): 1 - 5432
```

#### Clone Private Channel

```bash
# 1. Switch to USER mode
Dashboard → "👤 User Mode"

# 2. Join the channel (if not already a member)
/join https://t.me/+PrivateInviteLink

# 3. Clone the channel
/clone https://t.me/c/1234567890/100

# Bot uses your user account to access restricted content
```

#### Clone with Worker Pool

```bash
# 1. Add multiple worker bots
/connect 111111:AAA...
/connect 222222:BBB...
/connect 333333:CCC...

# 2. Clone large channel
/clone https://t.me/largechannel/1

# Workers distribute upload load = 3-5× faster!
```

#### Clone to Dump Channel

```bash
# 1. Create a Telegram channel
# 2. Add your bot as admin (with "Post Messages" permission)
# 3. Bot auto-detects and saves the channel

# 4. Clone sources — all go to dump channel
/clone https://t.me/source1/1
/clone https://t.me/source2/1
/clone https://t.me/source3/1

# All content appears in your dump channel automatically
```

### Clone vs Batch vs Single

| Feature | `/clone` | `/bdl` | `/dl` |
|---------|----------|--------|-------|
| **Target** | Entire channel (auto) | Custom range (manual) | Single message |
| **Input** | Any message link | Start + end links | One link |
| **Boundary Detection** | ✅ Automatic | ❌ Manual | N/A |
| **Best For** | Full channel archives | Specific sections | Individual files |
| **Setup Complexity** | Minimal (1 link) | Medium (2 links) | Minimal (1 link) |
| **Resume Support** | ✅ Yes | ✅ Yes | ❌ No |
| **Source Tracking** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Media Groups** | ✅ Preserved | ✅ Preserved | ✅ Preserved |

**When to use each:**
- **`/clone`** — Archive entire channels, migrate content, full backups
- **`/bdl`** — Download specific date ranges, selected portions
- **`/dl`** — Single videos, documents, or messages

### Real-World Use Cases

#### 1. Educational Content Archive

```bash
# Archive an educational channel for offline access
/clone https://t.me/programming_tutorials/1

# Use case: Students can access lectures offline
# Result: Complete course archive with all videos and PDFs
```

#### 2. News Channel Backup

```bash
# Backup a news channel for research purposes
/clone https://t.me/tech_news_daily/1

# Use case: Researcher analyzing news trends
# Result: Complete historical archive of all articles
```

#### 3. Media Collection Migration

```bash
# Move content from old channel to new channel

# 1. Set new channel as dump target
# 2. Clone old channel
/clone https://t.me/old_movie_channel/1

# Use case: Channel owner migrating to new account
# Result: All movies transferred to new channel
```

#### 4. Private Group Backup

```bash
# Backup restricted group content before it gets deleted

# 1. Switch to USER mode
# 2. Clone the group
/clone https://t.me/c/1234567890/1

# Use case: Preserving important group discussions
# Result: Complete backup of all messages and files
```

#### 5. Multiple Channel Aggregation

```bash
# Clone multiple related channels into one dump channel

# 1. Set up dump channel
# 2. Clone all sources
/clone https://t.me/science_news/1
/clone https://t.me/tech_updates/1
/clone https://t.me/research_papers/1

# Use case: Content curator aggregating sources
# Result: All content unified in single channel
```

### Source History Tracking

Every cloned channel is automatically tracked in source history:

#### Viewing Source History

```bash
# Via dashboard
/start → "📥 Sources" button

# Shows recent sources:
📥 Source Channel Manager

Recent Sources:
1. TechCommunity (1234567890)
2. ScienceNews (9876543210)
3. MovieArchive (5555555555)
4. ResearchPapers (1111111111)
...
```

#### Source History Storage

```
downloads/source_history.json:
[
  {
    "chat_id": -1001234567890,
    "title": "TechCommunity"
  },
  {
    "chat_id": -1009876543210,
    "title": "ScienceNews"
  },
  ...
]
```

**Benefits:**
- **Quick reference** to previously cloned channels
- **Audit trail** of content sources
- **Easy re-cloning** if needed
- **Dashboard integration** for management

### Progress Monitoring

#### Real-Time Updates

```
Clone in progress:
📥 Progress: 200 items. 📍 Current: 200
📥 Progress: 400 items. 📍 Current: 400
📥 Progress: 600 items. 📍 Current: 600
📥 Progress: 800 items. 📍 Current: 800
...
✅ Batch Complete! Total: 5,432 files
```

#### Dashboard Monitoring

```
🤖 Restricted Content Downloader
━━━━━━━━━━━━━━━━━━━━━
⚡ Active DLs: 3 | Tasks: 8
🤖 Worker Bots: 4 active
⏱ Uptime: 2h 15m 43s
💾 Storage: 12.4 GB free
🧠 RAM Load: 58%
━━━━━━━━━━━━━━━━━━━━━
📂 Destination: Channel -10012345
🛠 Current Mode: BOT
```

#### Log File Monitoring

```bash
# Download logs via bot
/logs

# Or view directly
tail -f logs.txt

# Log entries show:
# [DD-Mon-YY HH:MM:SS] - INFO - Processing message 1234
# [DD-Mon-YY HH:MM:SS] - INFO - Downloaded: video.mp4 (15.2 MB)
# [DD-Mon-YY HH:MM:SS] - INFO - Progress: 1234/5432 (22.7%)
```

### Crash Recovery

The clone system is **crash-safe** — if the bot crashes or server restarts, cloning automatically resumes.

#### How It Works

1. **State saved** after every message to `downloads/user_state.json`
2. **On restart**, bot detects incomplete batch
3. **Auto-resumes** from last processed message
4. **No data loss** — progress preserved

#### State File Example

```json
{
  "123456789": {
    "source": -1001234567890,
    "start": 1,
    "end": 5432,
    "current": 2847,
    "status": "active"
  }
}
```

**If bot crashes at message 2847:**
- Restart: `python main.py`
- Bot automatically resumes from 2848
- Remaining: 2,585 messages to download

#### Manual Resume Control

```bash
# Send /bdl without arguments to see resume options
/bdl

# Bot shows:
⚠️ Found Batch!
Source: TechCommunity
Range: 1 - 5432
Current: 2847

[ ▶️ Resume (2848) ]   ← Continue from 2848
[ 🔄 Start Over   ]    ← Restart from 1
[ ✖️ Cancel       ]    ← Clear saved state
```

### Performance Optimization

#### Speed Tips

| Strategy | Speed Gain | Implementation |
|----------|------------|----------------|
| **Add Worker Bots** | 3-5× faster | `/connect <token>` for each bot |
| **Use Dump Channel** | 20-30% faster | Add bot as channel admin |
| **Increase Concurrency** | 30-50% faster | `MAX_CONCURRENT_DOWNLOADS=5` |
| **BOT Mode** | 2× faster | Use for public channels |
| **Direct Forwarding** | 10× faster | Automatic for unprotected content |

#### Configuration Tuning

```env
# config.env optimizations

# Fast setup (may hit rate limits)
MAX_CONCURRENT_DOWNLOADS=5
FLOOD_WAIT_DELAY=0
BATCH_SIZE=200

# Balanced (recommended)
MAX_CONCURRENT_DOWNLOADS=3
FLOOD_WAIT_DELAY=2
BATCH_SIZE=200

# Conservative (slow but safe)
MAX_CONCURRENT_DOWNLOADS=1
FLOOD_WAIT_DELAY=5
BATCH_SIZE=100
```

### Troubleshooting

#### Clone Stopped Midway

**Symptoms:** Clone stops, no progress updates

**Solutions:**
1. Check bot status: `docker compose ps` or `systemctl status tgbypass`
2. Restart bot: `python main.py`
3. Bot auto-resumes from last position
4. Or manually: `/bdl` → "▶️ Resume"

#### Clone Too Slow

**Symptoms:** 1-2 files per minute

**Solutions:**
1. **Add worker bots:** `/connect <token>` (3-5 recommended)
2. **Use dump channel** instead of private chat
3. **Increase concurrency:** `MAX_CONCURRENT_DOWNLOADS=5`
4. **Switch to BOT mode** for public channels
5. **Check internet speed** — minimum 10 Mbps recommended

#### FloodWait Errors

**Symptoms:** "Please wait X seconds" errors

**Solutions:**
1. **Increase delay:** `FLOOD_WAIT_DELAY=5` or `10`
2. **Reduce concurrency:** `MAX_CONCURRENT_DOWNLOADS=2`
3. **Add more workers** to distribute load
4. **Wait it out** — bot retries automatically
5. **Use USER mode** — different rate limits

#### Can't Access Private Channel

**Symptoms:** "Chat not found" or "Access denied"

**Solutions:**
1. **Switch to USER mode:** Dashboard → "👤 User Mode"
2. **Join channel:** `/join https://t.me/+InviteLink`
3. **Verify SESSION_STRING** in config.env
4. **Check membership** — ensure your account has access
5. **Invite link valid?** — test in official Telegram app

#### Disk Full During Clone

**Symptoms:** Clone stops, "No space left" error

**Solutions:**
1. **Clean temp files:** `/clean`
2. **Check disk:** `df -h` shows free space
3. **Use dump channel** — reduces local storage need
4. **Increase disk space** — 20GB minimum for large clones
5. **Clone in batches** — use `/bdl` for smaller ranges

### Best Practices

#### Before Cloning

✅ **DO:**
- Check available disk space (20GB+ for large channels)
- Add worker bots for large channels (1000+ messages)
- Set up dump channel for organized output
- Switch to USER mode for private content
- Verify bot has necessary permissions

❌ **DON'T:**
- Clone without checking disk space
- Use aggressive settings (may trigger bans)
- Clone copyrighted content illegally
- Exceed Telegram's rate limits repeatedly
- Share your SESSION_STRING

#### During Cloning

✅ **DO:**
- Monitor dashboard for progress
- Check logs for errors: `/logs`
- Let bot handle FloodWait automatically
- Keep bot running until completion

❌ **DON'T:**
- Stop/restart unnecessarily
- Change settings mid-clone
- Delete state files manually
- Interrupt deliberately

#### After Cloning

✅ **DO:**
- Verify completion notification
- Clean temp files: `/clean`
- Review cloned content
- Update source history if needed

❌ **DON'T:**
- Delete dump channel immediately
- Lose track of source attribution
- Forget to backup important content
- Violate content creator rights

### Advanced Techniques

#### Parallel Channel Cloning

```bash
# Method 1: Sequential (one after another)
/clone https://t.me/channel1/1  # Wait for completion
/clone https://t.me/channel2/1  # Then start next

# Method 2: Multiple bot instances (advanced)
# Run separate bot instances with different configs
# Each clones a different channel simultaneously
```

#### Selective Cloning

```bash
# Clone only recent messages
/bdl https://t.me/channel/9000 https://t.me/channel/10000

# Clone specific sections
/bdl https://t.me/channel/1 https://t.me/channel/1000    # Part 1
/bdl https://t.me/channel/1001 https://t.me/channel/2000 # Part 2
```

#### Scheduled Cloning

```bash
# Use cron (Linux) for automated daily clones
crontab -e

# Add:
0 2 * * * cd /path/to/bot && ./venv/bin/python main.py --clone-url https://t.me/news/1

# Or use systemd timers for more control
```

### Summary

The Smart Clone System is designed for **effortless channel archiving**:

- **One command** — no complex setup
- **Automatic** — discovers boundaries for you
- **Reliable** — crash-safe with auto-resume
- **Fast** — parallel processing with workers
- **Tracked** — source history for all clones

**Start cloning channels today with just:** `/clone <link>`

---

## 🔄 Multi-Bot Worker Pool

### How Worker Selection Works

```
New download task arrives
          │
          ▼
   round_robin(WORKER_POOL)
          │
          ├── worker.is_connected? ──No──► try next worker
          │
          └── Yes ──► task assigned to this worker
                              │
                              ▼
                   Download + upload complete
                              │
                              ▼
                   Semaphore slot released
```

Workers rotate in a strict round-robin cycle. Each task gets the next available, connected worker.

### Persistence Across Restarts

Worker bots added via `/connect` are written to `downloads/extra_bots.txt`. On every startup, the bot reads this file and reconnects all saved workers. **You never need to re-add workers after a restart.**

### Automatic Failure Handling

If a worker's token becomes invalid (bot deleted, token revoked):
1. An `AuthKeyUnregistered` or `AccessTokenInvalid` exception is caught
2. The worker is automatically removed from the pool
3. The download is retried using another worker
4. An error is logged for your review

### Worker Count Guidelines

| Use case | Recommended workers |
|---|---|
| Personal / occasional use | 1 (just the main bot) |
| Regular batches (< 1,000 files) | 2–3 workers |
| Heavy batches (1,000–10,000 files) | 3–5 workers |
| Production scale (10,000+ files) | 5+ workers |

---

## 📁 Project Structure & Runtime Files

### Source Files

```
TelegramRestrictionBypass/
│
├── main.py                ← Entry point: initialization, handlers, core download logic
├── config.py              ← Reads config.env into the PyroConf class
├── logger.py              ← Rotating file logger + console output setup
│
├── helpers/
│   ├── files.py           ← Download path creation, size validation, cleanup
│   ├── msg.py             ← Telegram link parsing, caption formatting, filename detection
│   ├── settings.py        ← Persistent ConfigManager (speed, mode, auth users, dump chat)
│   ├── state.py           ← StateManager — batch progress for crash-safe auto-resume
│   └── utils.py           ← Media group handling, send_media, ffprobe thumbnails
│
├── requirements.txt       ← Python package dependencies
├── config.env             ← YOUR CREDENTIALS — never commit this!
├── Dockerfile             ← Docker image definition (python:3.11-slim base)
├── docker-compose.yml     ← Docker Compose service (host network, always restart)
└── README.md              ← This file
```

### Runtime Files in `downloads/`

| File | Created By | Contains | Effect of Deleting |
|---|---|---|---|
| `owner_id.txt` | First `/start` | Owner's Telegram user ID | Next `/start` claims a new owner |
| `settings.json` | Dashboard config changes | Speed, delay, mode, authorized users | Reverts all to defaults |
| `dump_target.txt` | Bot promoted in a channel | Target channel ID for forwarding | Clears dump channel |
| `extra_bots.txt` | Each `/connect` | Extra bot tokens, one per line | Workers not reloaded on restart |
| `user_state.json` | Every batch start | Per-user batch progress | Disables auto-resume for all users |
| `history.txt` | Reserved | Download history log | Safe to delete |

### What Never to Commit

Ensure `.gitignore` covers these:

```gitignore
config.env
downloads/
*.session
logs.txt
__pycache__/
venv/
.env
```

---

## 🐛 Bug Fixes in This Release

Six bugs were identified during code audit and fixed:

<table>
<tr>
<th>#</th>
<th>File</th>
<th>Bug</th>
<th>Fix</th>
</tr>
<tr>
<td><b>1</b></td>
<td><code>main.py</code></td>
<td><b>AttributeError crash</b> — <code>client.me</code> in <code>on_chat_member_updated</code> can be <code>None</code> before <code>get_me()</code> is called, causing a crash the first time any bot is added to a channel</td>
<td>Changed to <code>bot.me.id</code> — the module-level <code>bot</code> object is fully initialized before any handlers fire</td>
</tr>
<tr>
<td><b>2</b></td>
<td><code>main.py</code></td>
<td><b>Unhandled callback</b> — the Bot Manager panel renders buttons with <code>callback_data="bot_info_*"</code> but the callback handler had no <code>bot_info_*</code> case. Clicking any bot's name caused an infinite spinning loader with no response</td>
<td>Added a full <code>bot_info_*</code> handler displaying the bot's name, Telegram ID, username, role (Main/Worker), and live connection status</td>
</tr>
<tr>
<td><b>3</b></td>
<td><code>main.py</code></td>
<td><b>Missing <code>query.answer()</code></b> on 6 callbacks — <code>refresh_dash</code>, <code>manage_bots</code>, <code>open_settings</code>, <code>send_logs</code> (success path), <code>resume_batch</code>, <code>restart_batch</code> — all left a spinning loader forever on Telegram mobile clients</td>
<td>Added <code>await query.answer(...)</code> with descriptive status text to every affected callback</td>
</tr>
<tr>
<td><b>4</b></td>
<td><code>main.py</code></td>
<td><b>Env vars silently ignored</b> — <code>MAX_CONCURRENT_DOWNLOADS</code>, <code>FLOOD_WAIT_DELAY</code>, and <code>BATCH_SIZE</code> were parsed into <code>PyroConf</code> but never applied to <code>Config</code>. Any values set in <code>config.env</code> had zero effect at runtime</td>
<td>Added explicit <code>Config.set(...)</code> calls in <code>initialize()</code> to apply all three env vars to the runtime config before the asyncio semaphore is created</td>
</tr>
<tr>
<td><b>5</b></td>
<td><code>helpers/utils.py</code></td>
<td><b>Premium users blocked at upload</b> — <code>send_media()</code> called <code>fileSizeLimit(..., is_premium=False)</code> unconditionally. Premium users' large files that passed the download size check would then fail the upload size check</td>
<td>Added <code>is_premium</code> parameter to <code>send_media()</code> signature and propagated it from <code>safe_download()</code> where premium status is already correctly determined</td>
</tr>
<tr>
<td><b>6</b></td>
<td><code>helpers/utils.py</code></td>
<td><b>Album files downloaded to wrong directory</b> — <code>processMediaGroup()</code> called <code>await msg.download()</code> with no <code>file_name</code> argument, causing Pyrogram to save album items to the current working directory (project root) with random generated names instead of the organized <code>downloads/album_*/</code> structure</td>
<td>Now calls <code>get_download_path(f"album_{media_group_id}", fname)</code> exactly as <code>safe_download()</code> does, placing album items in the correct organized subdirectory and enabling proper cleanup</td>
</tr>
</table>

---

## 🛠️ Troubleshooting

<details>
<summary><b>❌ "API_ID must be a numeric value" or "API_HASH is not configured properly"</b></summary>

**What it means:** You haven't filled in your Telegram credentials in `config.env`, or they contain placeholder text.

**Fix:**
1. Open `config.env` in a text editor:
   ```bash
   nano config.env
   ```
2. Replace the placeholder values:
   - `API_ID=YOUR_API_ID_HERE` → `API_ID=12345678` (your actual numeric ID)
   - `API_HASH=YOUR_API_HASH_HERE` → `API_HASH=abc123...` (your actual hash)
   - `BOT_TOKENS=YOUR_BOT_TOKEN_HERE` → `BOT_TOKENS=1234567890:ABC...` (your bot token)
3. Save and restart the bot

See [Getting Your Credentials](#-getting-your-credentials) for detailed instructions on obtaining these values.

</details>

<details>
<summary><b>❌ "ModuleNotFoundError: No module named 'psutil'" or similar import errors</b></summary>

**What it means:** Python dependencies are not installed.

**Fix:**
```bash
pip install -r requirements.txt
```

If using a virtual environment (recommended), make sure it's activated first:
```bash
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

</details>

<details>
<summary><b>❌ "User Session failed to start" in logs</b></summary>

**What it means:** The `SESSION_STRING` is invalid, expired, or the account was deauthorized.

**Fix:**
1. Re-generate a fresh session string (see [Getting Your Credentials → Session String](#3-session-string))
2. Replace in `config.env` and restart

The bot continues running in BOT-only mode even if the user session fails — everything except USER Mode still works.

</details>

<details>
<summary><b>❌ Frequent FloodWait errors slowing everything down</b></summary>

**Fix (in order of impact):**
1. **Add more worker bots** via `/connect` — more bots spread the API load
2. **Increase delay:** `FLOOD_WAIT_DELAY=5` or `10` in `config.env`
3. **Reduce concurrency:** `MAX_CONCURRENT_DOWNLOADS=2` in `config.env`
4. **Wait** — FloodWait is temporary (5–60s). The bot retries automatically up to 5 times.

</details>

<details>
<summary><b>❌ ConnectionResetError / frequent disconnections (AWS / Debian)</b></summary>

**Fix:**
```bash
# Disable IPv6 immediately
sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1

# Make permanent
echo "net.ipv6.conf.all.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
echo "net.ipv6.conf.default.disable_ipv6 = 1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
sudo systemctl restart tgbypass
```

</details>

<details>
<summary><b>❌ MD5_CHECKSUM_INVALID during download</b></summary>

**What it means:** A data chunk was corrupted in transit — usually network instability.

**Fix:**
- Bot retries automatically up to 2 times
- Verify TgCrypto is installed: `pip show TgCrypto`
- For persistent errors: consider a server physically closer to Telegram's DCs (Frankfurt, Amsterdam, Singapore, Miami)

</details>

<details>
<summary><b>❌ Disk fills up quickly</b></summary>

**Fix:**
```bash
# Via bot (safest — preserves state files)
/clean

# Via shell (keeps .txt and .json)
find downloads/ -type f ! -name "*.txt" ! -name "*.json" -delete

# Nuclear (only when bot is stopped)
rm -rf downloads/
```

</details>

<details>
<summary><b>❌ Bot doesn't respond to commands</b></summary>

**Check in order:**

1. Is it running?
   ```bash
   sudo systemctl status tgbypass  # systemd
   docker compose ps               # Docker
   ```
2. Are you messaging it in **private chat**? (All commands are private-only)
3. Is your user ID authorized? (First `/start` claims ownership)
4. Are credentials correct in `config.env`?
5. Check the logs:
   ```bash
   sudo journalctl -u tgbypass -n 50
   docker compose logs --tail=50
   tail -n 50 logs.txt
   ```

</details>

<details>
<summary><b>❌ Batch stopped midway; auto-resume didn't trigger</b></summary>

**Diagnose:**
```bash
cat downloads/user_state.json
# Expected: {"123456": {"source": -100123, "start": 100, "end": 5000, "current": 847, "status": "active"}}
```

**Fix if file is corrupted:**
```bash
rm downloads/user_state.json    # clear corrupted state (stop bot first)
# Then restart and manually resume:
/bdl https://t.me/channel/847 https://t.me/channel/5000
```

</details>

<details>
<summary><b>❌ "Access Denied" when sending commands</b></summary>

1. Find your Telegram user ID: message [@userinfobot](https://t.me/userinfobot)
2. Have the bot owner run: `/auth YOUR_ID`
3. Or if you are the owner but lost access: stop bot, delete `downloads/owner_id.txt`, restart, `/start`

</details>

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are all welcome.

**Development setup:**

```bash
git clone https://github.com/YOUR_USERNAME/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass
python3.11 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
git checkout -b feature/my-feature
```

**Guidelines:**
- Follow PEP 8 — lint with `flake8` or `ruff`
- Keep utility logic in `helpers/` — not in `main.py`
- Test with both BOT Mode and USER Mode
- Update this README if you add config variables, commands, or runtime files
- One logical change per commit, atomic commits

**When reporting bugs, include:**
- Python version (`python3 --version`)
- Deployment method (local, Docker, systemd)
- Relevant lines from `logs.txt`
- Steps to reproduce

---

## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for full terms.

---

## 👨‍💻 Credits

<div align="center">

### Primary Developer
**[@Paidguy](https://github.com/Paidguy)**

### Original Project
**[RestrictedContentDL](https://github.com/bisnuray/RestrictedContentDL)** by **[@bisnuray](https://github.com/bisnuray)**

### Core Libraries
[Pyrofork](https://github.com/KurimuzonAkuma/pyrogram) &nbsp;·&nbsp; [TgCrypto](https://github.com/pyrogram/tgcrypto) &nbsp;·&nbsp; [Pyleaves](https://github.com/1Danish-00/pyleaves) &nbsp;·&nbsp; [python-dotenv](https://github.com/theskumar/python-dotenv)

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-@Paidguy-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Paidguy)
[![Telegram](https://img.shields.io/badge/Telegram-@Paidguy-0088cc?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/paidguy)
[![Original Repo](https://img.shields.io/badge/Original-RestrictedContentDL-FF6B35?style=for-the-badge&logo=github&logoColor=white)](https://github.com/bisnuray/RestrictedContentDL)

*If this helped you, please ⭐ both this repo and the [original](https://github.com/bisnuray/RestrictedContentDL)!*

</div>

---

## ⚠️ Legal Disclaimer

<div align="center">

```
╔══════════════════════════════════════════════════════════╗
║     FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY          ║
╚══════════════════════════════════════════════════════════╝
```

</div>

**Terms of Service:** This software may violate [Telegram's Terms of Service](https://telegram.org/tos), which prohibit circumventing content restrictions. Use may result in permanent suspension of any associated Telegram accounts or bots.

**Copyright Law:** Downloading or redistributing restricted content without authorization may infringe intellectual property rights and violate laws including the DMCA (US), EU Copyright Directive, Computer Misuse Act (UK), and equivalent legislation worldwide.

**Your Responsibility:** You are **solely responsible** for verifying legal compliance in your jurisdiction, obtaining proper authorization before downloading content, and any consequences — legal, financial, or otherwise — that result from your use. The developers disclaim all liability.

**Permitted Use Only:** Content you own, have explicit written permission to download, authorized academic/security research, or development testing in isolated environments.

```diff
- Pirating or redistributing copyrighted content
- Bypassing restrictions on content you don't own
- Any activity that violates applicable law
```

> 🚨 If in doubt about legality, consult a qualified legal professional **before** using this software.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1f2e,50:161b22,100:0d1117&height=120&section=footer&text=Use%20Responsibly&fontSize=24&fontColor=58a6ff&fontAlignY=65&animation=twinkling" width="100%"/>

**Built with [Pyrofork](https://github.com/KurimuzonAkuma/pyrogram) · Powered by Python 3.11 · Use Responsibly**

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3500&pause=1000&color=58A6FF&center=true&vCenter=true&width=500&lines=📚+Complete+Documentation;⚡+Production-Ready+Features;🔒+Secure+%26+Reliable;🚀+Fast+%26+Efficient" alt="Footer Animation" />

<br/>

*Last updated: February 2026*

</div>
