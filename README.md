# TelegramRestrictionBypass

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![Library](https://img.shields.io/badge/library-Pyrogram-orange)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## ⚠️ LEGAL DISCLAIMER & WARNING

**READ THIS CAREFULLY BEFORE USING THIS SOFTWARE**

This software is provided **FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**. By downloading, installing, or using this software, you acknowledge and agree to the following:

### Legal & Ethical Warnings

1. **Telegram Terms of Service**: Using this software may violate [Telegram's Terms of Service](https://telegram.org/tos). Telegram explicitly prohibits bypassing content restrictions and security features.

2. **Copyright Infringement**: Downloading, copying, or redistributing restricted content may violate copyright laws in your jurisdiction. Content creators use restrictions to protect their intellectual property rights.

3. **Legal Liability**: Users of this software are **solely responsible** for ensuring their use complies with all applicable local, national, and international laws. This includes but is not limited to:
   - Copyright and intellectual property laws
   - Digital Millennium Copyright Act (DMCA) in the United States
   - EU Copyright Directive
   - Computer Fraud and Abuse Act
   - Other anti-circumvention legislation

4. **Account Bans**: Using this software may result in permanent suspension or termination of your Telegram account(s).

5. **Criminal Penalties**: In some jurisdictions, circumventing access controls or technological protection measures may result in criminal prosecution, fines, and imprisonment.

### No Warranty or Liability

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. THE AUTHORS AND COPYRIGHT HOLDERS:

- **DISCLAIM ALL LIABILITY** for any damages, losses, or legal consequences arising from the use or misuse of this software
- **DO NOT ENCOURAGE, ENDORSE, OR CONDONE** any illegal use of this software
- **ARE NOT RESPONSIBLE** for how you choose to use this software
- **PROVIDE NO LEGAL PROTECTION** or defense for users who face legal action

### User Responsibility

**YOU ARE SOLELY RESPONSIBLE FOR:**
- Understanding and complying with all applicable laws in your jurisdiction
- Obtaining proper authorization before accessing or downloading content
- Respecting content creators' rights and restrictions
- Any legal consequences that result from your use of this software
- Any account suspensions or bans

### Recommended Legal Use Cases

This software should only be used for:
- **Educational research** into Telegram API functionality
- **Personal archival** of content you own or have explicit permission to download
- **Security research** with proper authorization
- **Backup purposes** for your own content

**DO NOT USE THIS SOFTWARE TO:**
- Pirate or redistribute copyrighted content
- Bypass restrictions on content you don't own
- Violate any platform's terms of service
- Engage in any illegal activity

---

## 📋 Overview

This is a Python-based bot built with Pyrogram that demonstrates how content restrictions work on Telegram. It shows the technical process of downloading and re-uploading media from channels where saving is restricted.

### Features

- Asynchronous content processing
- FloodWait handling to manage rate limits
- Multi-account rotation support
- Automatic cleanup of temporary files
- Built with Pyrogram 2.0 and TgCrypto for performance

## 🔧 Technical Requirements

- Python 3.11 or higher
- Telegram API credentials (API_ID and API_HASH from [my.telegram.org](https://my.telegram.org))
- Session string for authentication
- Sufficient server storage and bandwidth

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Paidguy/TelegramRestrictionBypass
cd TelegramRestrictionBypass
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file or edit `config.env`:

```env
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
SESSION_STRING=your_session_string
```

### 4. Deploy

**For development:**
```bash
python main.py
```

**For production (with screen):**
```bash
screen -S telegram_bot
python main.py
# Press Ctrl+A then D to detach
```

**Using Docker:**
```bash
docker-compose up -d
```

## 📖 How It Works

1. User sends a Telegram message link to the bot
2. Bot authenticates and accesses the linked content
3. Content is downloaded to local storage
4. Metadata is processed and restrictions are removed
5. File is re-uploaded to the user as a standard message
6. Temporary files are automatically cleaned up

## 🛠 Architecture

- **main.py**: Core bot logic and message handlers
- **config.py**: Configuration management
- **logger.py**: Logging system
- **helpers/**: Utility functions for download/upload operations

## ⚙️ Configuration Options

Customize behavior in `config.env`:
- `MAX_CONCURRENT_DOWNLOADS`: Limit simultaneous downloads
- `AUTO_DELETE_TIMEOUT`: Time before temporary files are removed
- `FLOOD_WAIT_MULTIPLIER`: Adjustment factor for rate limit handling

## 🐛 Troubleshooting

**Connection Errors on AWS:**
- Disable IPv6 if experiencing connectivity issues
- Ensure security groups allow Telegram API ports

**MD5 Checksum Errors:**
- The bot includes automatic retry logic
- Check network stability

**Disk Space Issues:**
- Enable automatic cleanup in configuration
- Monitor available storage

## 🤝 Contributing

Contributions for educational purposes are welcome. Please ensure any modifications:
- Maintain the legal disclaimer
- Include proper error handling
- Follow Python best practices
- Add appropriate documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: The MIT License does NOT provide any protection against legal liability for misuse. Users are independently responsible for their actions.

## 🔗 Resources

- [Telegram Terms of Service](https://telegram.org/tos)
- [Pyrogram Documentation](https://docs.pyrogram.org/)
- [Telegram API Documentation](https://core.telegram.org/api)

## ⚖️ Final Warning

**This software is a tool. Like any tool, it can be used responsibly or irresponsibly. The developers provide this for educational purposes and take no responsibility for misuse. If you choose to use this software, you do so at your own risk and legal liability.**

**When in doubt, consult with a legal professional in your jurisdiction before using this software.**

---

*Last Updated: December 2025*
