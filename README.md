# 🚀 TelegramRestrictionBypass

<div align="center">

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-green.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

**Production-grade Telegram content downloader with multi-bot worker pools, crash-safe auto-resume, and dual BOT/USER modes**

[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Documentation](#-documentation) • [Support](#-support)

</div>

---

## 📖 Overview

TelegramRestrictionBypass is a powerful, production-ready Telegram bot that downloads and re-uploads content from Telegram channels—including restricted content. Built with scalability and reliability in mind, it features:

- **🤖 Multi-Bot Worker Pools** - Round-robin distribution for parallel uploads
- **💾 Crash-Safe Auto-Resume** - Automatically continues interrupted batch downloads
- **🔄 Dual Download Modes** - BOT mode (public) + USER mode (restricted/private)
- **📊 Live Admin Dashboard** - Real-time stats, controls, and monitoring
- **🎯 Smart Media Handling** - Albums stay intact, proper metadata preservation
- **⚡ High Performance** - Concurrent downloads, TgCrypto acceleration
- **🛡️ Production Features** - FloodWait handling, worker failover, persistent state

Perfect for archiving channels, downloading media collections, or building content aggregation workflows at scale.

---

## ✨ Features

### Core Functionality

| Feature | Description |
|---------|-------------|
| **Single Download** | `/dl <link>` - Download any one Telegram message |
| **Batch Download** | `/bdl <start> <end>` - Download thousands of messages in a range |
| **BOT Mode** | Uses bot tokens to fetch public channel content |
| **USER Mode** | Uses your Telegram account to access restricted/private channels |
| **Media Groups** | Albums are kept intact and re-uploaded together |
| **Auto-Resume** | Interrupted batches restart automatically on system reboot |

### Production-Grade Features

✅ **Multi-Bot Worker Pool** - Add unlimited worker bots for parallel uploads
✅ **Live Dashboard** - Real-time RAM, storage, uptime, and worker stats
✅ **Dump Channel** - Forward all downloads to a Telegram channel instead of private chat
✅ **FloodWait Handling** - Exponential backoff with automatic retry (up to 5 attempts)
✅ **User Authorization** - Owner-only by default, authorize additional users via `/auth`
✅ **Persistent Settings** - Configuration survives restarts (`downloads/settings.json`)
✅ **Crash Recovery** - Batch state saved to `user_state.json` for seamless resume
✅ **Automatic Cleanup** - Temp files removed after upload and on startup
✅ **Rotating Logs** - Max 10MB with auto-purge, keeps system clean

### Technical Highlights

- **TgCrypto Acceleration** - Fast C-level encryption (~10x faster)
- **Asyncio Concurrency** - Semaphore-controlled parallel downloads
- **FFmpeg Integration** - Video metadata extraction and thumbnail generation
- **Worker Pool Failover** - Bad tokens automatically removed
- **Progress Bars** - Beautiful upload/download indicators with Pyleaves
- **IPv6 Disabled** - Optimized for cloud environments (AWS compatible)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Telegram account
- API credentials from [my.telegram.org](https://my.telegram.org)
- Bot token from [@BotFather](https://t.me/BotFather)

### 5-Minute Setup

```bash
# 1. Clone repository
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass

# 2. Install dependencies
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure
cp config.env.example config.env
nano config.env  # Add your API_ID, API_HASH, BOT_TOKEN

# 4. Run
python main.py
```

Send `/start` to your bot in Telegram, and you're ready! 🎉

For detailed installation, see [📚 Installation Guide](docs/INSTALLATION.md)

---

## 🐳 Docker Deployment

### Quick Docker Start

```bash
# 1. Clone and configure
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass
cp config.env.example config.env
nano config.env  # Add credentials

# 2. Build and run
docker compose up -d --build

# 3. View logs
docker compose logs -f
```

**Benefits:**
- ✅ Isolated environment
- ✅ No dependency conflicts
- ✅ Easy updates (`docker compose pull && docker compose up -d`)
- ✅ Production-ready

For Docker details, see [🐳 Docker Guide](docs/DOCKER.md)

---

## 📚 Documentation

### Getting Started
- **[📥 Installation Guide](docs/INSTALLATION.md)** - Complete setup for fresh machines
- **[⚡ Quick Start](docs/QUICKSTART.md)** - 5-minute condensed guide
- **[⚙️ Setup & Configuration](docs/SETUP.md)** - Detailed configuration reference
- **[📦 Dependencies](docs/DEPENDENCIES.md)** - All packages and system requirements

### Full Documentation
- **[📖 Complete Documentation](docs/README.md)** - Comprehensive guide with all features
- **[🐳 Docker Guide](docs/DOCKER.md)** - Container deployment
- **[🔧 Troubleshooting](docs/README.md#troubleshooting)** - Common issues and solutions
- **[🤝 Contributing](CONTRIBUTING.md)** - Development guidelines

---

## 🎯 Usage

### Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Open dashboard | `/start` |
| `/dl <link>` | Download single message | `/dl https://t.me/channel/12345` |
| `/bdl <start> <end>` | Batch download range | `/bdl https://t.me/c/123/100 https://t.me/c/123/500` |
| `/connect <token>` | Add worker bot | `/connect 123456:ABC-DEF...` |
| `/join <link>` | Join channel (USER mode) | `/join https://t.me/privatechannel` |
| `/auth <uid>` | Authorize user (owner only) | `/auth 987654321` |
| `/logs` | Get log file | `/logs` |
| `/clean` | Clean temp files | `/clean` |

### Dashboard Features

The interactive dashboard provides:
- **🔄 Refresh** - Update stats in real-time
- **⚙️ Settings** - Adjust speed and delays
- **🤖 Manage Bots** - Add/remove worker bots
- **👤/🤖 Toggle Mode** - Switch between BOT and USER modes
- **📜 Logs** - Download log file
- **🛑 STOP ALL** - Kill all running downloads

---

## 🛠️ Configuration

### Environment Variables

Create `config.env` with your credentials:

```bash
# Telegram API (from my.telegram.org)
API_ID=12345678
API_HASH=your_api_hash_here

# Bot Token (from @BotFather)
BOT_TOKENS=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11

# Optional: Add multiple worker bots (comma-separated)
# BOT_TOKENS=token1,token2,token3

# Optional: User Session (for restricted content)
SESSION_STRING=your_session_string_here

# Performance Tuning (optional)
MAX_CONCURRENT_DOWNLOADS=5
FLOOD_WAIT_DELAY=2
BATCH_SIZE=200
```

### Getting Credentials

1. **API_ID & API_HASH**: Visit [my.telegram.org](https://my.telegram.org) → API Development Tools
2. **BOT_TOKEN**: Message [@BotFather](https://t.me/BotFather) → `/newbot`
3. **SESSION_STRING**: See [Setup Guide](docs/SETUP.md#generating-session-string)

---

## 📊 Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     TelegramRestrictionBypass                │
│                                                              │
│  ┌─────────────┐      ┌──────────────┐      ┌────────────┐ │
│  │  Main Bot   │◄─────┤  User Client │◄─────┤ Telegram   │ │
│  │  (Control)  │      │  (Download)  │      │  MTProto   │ │
│  └──────┬──────┘      └──────────────┘      └────────────┘ │
│         │                                                    │
│         │ Coordinates                                        │
│         ▼                                                    │
│  ┌──────────────────────────────────────────┐               │
│  │         Worker Pool (Round-Robin)        │               │
│  │  ┌────────┐ ┌────────┐ ┌────────┐       │               │
│  │  │ Bot 1  │ │ Bot 2  │ │ Bot N  │  ...  │               │
│  │  └───┬────┘ └───┬────┘ └───┬────┘       │               │
│  └──────┼──────────┼──────────┼────────────┘               │
│         │          │          │                             │
│         └──────────┴──────────┴─► Upload to User/Channel   │
│                                                              │
│  ┌──────────────────────────────────────────┐               │
│  │        Persistent State Layer            │               │
│  │  • settings.json    • user_state.json    │               │
│  │  • owner_id.txt     • extra_bots.txt     │               │
│  └──────────────────────────────────────────┘               │
└──────────────────────────────────────────────────────────────┘
```

**Flow:**
1. User sends command → Main bot receives
2. Fetch content → User client (USER mode) or Worker bot (BOT mode)
3. Download → Local temp storage with progress tracking
4. Upload → Next available worker from pool
5. Cleanup → Remove temp files, update state

---

## 🔧 Advanced Features

### Multi-Bot Worker Pool

Add unlimited worker bots for parallel uploads:

```bash
/connect 123456:ABC-DEF1234...
/connect 789012:XYZ-GHI5678...
```

**Benefits:**
- Distribute upload load across multiple bots
- Bypass rate limits more effectively
- Automatic failover if a bot fails
- Round-robin selection for fairness

### Batch Auto-Resume

If the bot crashes during a batch download:

1. Restart the bot: `python main.py`
2. Progress automatically resumes from last saved message
3. Send `/bdl` to see resume options

**State saved to:** `downloads/user_state.json`

### Dump Channel

Forward all downloads to a Telegram channel:

1. Create a channel and add your bot as admin
2. Bot automatically detects and saves channel ID
3. All downloads now go to channel instead of private chat

**Switch back:** Remove bot from channel or use settings

---

## 🎓 Use Cases

- **📚 Channel Archiving** - Backup entire Telegram channels
- **🎬 Media Collection** - Download video/photo series
- **📰 Content Aggregation** - Collect posts from multiple sources
- **🔄 Cross-Channel Reposting** - Re-upload content to your channel
- **💾 Personal Backups** - Save important messages locally
- **📖 Research** - Archive educational content for offline access

---

## ⚠️ Legal Disclaimer

This tool is provided for **educational and research purposes only**.

- ✅ **Allowed:** Downloading your own content, authorized channels, public information
- ❌ **Not Allowed:** Copyright infringement, unauthorized content distribution, violating Telegram ToS
- 📜 **Your Responsibility:** Ensure you have permission to download and redistribute content

**Important:**
- Respect copyright laws in your jurisdiction
- Follow Telegram's Terms of Service
- Use responsibly and ethically
- The developers are not responsible for misuse

---

## 🐛 Bug Reports & Issues

Found a bug? [Open an issue](https://github.com/Paidguy/TelegramRestrictionBypass/issues) with:

- Python version and OS
- Error logs (remove sensitive info)
- Steps to reproduce
- Expected vs actual behavior

### Known Bugs Fixed

This version includes fixes for:
- ✅ Undefined variable `is_prem` in upload verification
- ✅ Missing `query.answer()` on callbacks
- ✅ Album files downloaded to wrong directory
- ✅ Environment variables not applied
- ✅ Premium user file size checks
- ✅ Client initialization errors

See [Release Notes](docs/README.md#bug-fixes) for full list.

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass

# Install dev dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Make changes
git checkout -b feature/your-feature

# Test and commit
black .
flake8 .
git commit -m "Add feature: description"

# Push and create PR
git push origin feature/your-feature
```

---

## 🙏 Credits

### Original Author
- **[@bisnuray](https://github.com/bisnuray)** - Original [RestrictedContentDL](https://github.com/bisnuray/RestrictedContentDL)

### Enhanced By
- **[@Paidguy](https://github.com/Paidguy)** - Production features, bug fixes, enhancements

### Built With
- [Pyrofork](https://github.com/Mayuri-Chan/pyrofork) - Telegram MTProto client
- [TgCrypto](https://github.com/pyrogram/tgcrypto) - Encryption acceleration
- [FFmpeg](https://ffmpeg.org/) - Media processing

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Paidguy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 📞 Support

### Resources
- 📖 [Full Documentation](docs/README.md)
- 🐛 [Issue Tracker](https://github.com/Paidguy/TelegramRestrictionBypass/issues)
- 💬 [Discussions](https://github.com/Paidguy/TelegramRestrictionBypass/discussions)

### Community
- 📢 [Telegram Channel](https://t.me/itsSmartDev) - Updates and announcements
- 💡 [Stack Overflow](https://stackoverflow.com/questions/tagged/pyrogram) - Pyrofork/Pyrogram questions

---

## 🌟 Star History

If this project helped you, please give it a ⭐ star!

[![Star History](https://img.shields.io/github/stars/Paidguy/TelegramRestrictionBypass?style=social)](https://github.com/Paidguy/TelegramRestrictionBypass/stargazers)

---

## 📈 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/Paidguy/TelegramRestrictionBypass)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Paidguy/TelegramRestrictionBypass)
![Lines of code](https://img.shields.io/tokei/lines/github/Paidguy/TelegramRestrictionBypass)
![GitHub last commit](https://img.shields.io/github/last-commit/Paidguy/TelegramRestrictionBypass)

---

<div align="center">

**Made with ❤️ by [Paidguy](https://github.com/Paidguy)**

**Based on [RestrictedContentDL](https://github.com/bisnuray/RestrictedContentDL) by [@bisnuray](https://github.com/bisnuray)**

[⬆ Back to Top](#-telegramrestrictionbypass)

</div>
