# ⚡ Quick Start Checklist

**Want to get started FAST?** Follow this checklist, then see [SETUP.md](SETUP.md) for details.

---

## ✅ Setup Checklist

### 1️⃣ Prerequisites (5 minutes)

```bash
# Check Python version (need 3.11+)
python3 --version

# Install if needed (Ubuntu/Debian)
sudo apt update && sudo apt install python3.11 python3.11-venv python3-pip git -y
```

---

### 2️⃣ Get Credentials (10 minutes)

**API Credentials:**
1. Go to https://my.telegram.org
2. Login with your phone number
3. Click "API development tools"
4. Create app → Copy `api_id` and `api_hash`

**Bot Token:**
1. Open Telegram → Find @BotFather
2. Send `/newbot`
3. Follow prompts → Copy token

**Session String (optional):**
- Skip if only downloading public content
- See [SETUP.md - Step 3](SETUP.md#step-3-get-session_string-optional---for-user-mode) for generating

---

### 3️⃣ Install (5 minutes)

```bash
# Clone
git clone https://github.com/Paidguy/TelegramRestrictionBypass.git
cd TelegramRestrictionBypass

# Setup environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Configure (2 minutes)

```bash
# Edit config
nano config.env
```

**Replace these values:**
```env
API_ID=12345678                                   # ← Your numeric API ID
API_HASH=abc123def456...                          # ← Your API hash
BOT_TOKENS=1234567890:ABCdef...                   # ← Your bot token
SESSION_STRING=BQAx...                            # ← Your session (or leave empty)
```

**Save:** `Ctrl+X` → `Y` → `Enter`

---

### 5️⃣ Run (1 minute)

```bash
# Start the bot
python3 main.py
```

**Expected output:**
```
[INFO] - System Starting...
[INFO] - Starting User Session...
[INFO] - Initializing Bots...
```

---

### 6️⃣ Test (2 minutes)

1. Open Telegram
2. Find your bot (search for the username you created)
3. Send `/start`
4. You should see the dashboard! 🎉

**Test download:**
```
/dl https://t.me/durov/123
```

---

## 🎯 Total Time: ~25 minutes

## ❌ Having Issues?

### "API_ID must be a numeric value"
→ Edit `config.env` and remove quotes/placeholder text

### "ModuleNotFoundError"
→ Run: `pip install -r requirements.txt`

### "BOT_TOKENS must be set"
→ Make sure you pasted the actual bot token in config.env

### Bot doesn't respond
→ Make sure you clicked START in Telegram first

---

## 📖 Need More Help?

- **Detailed instructions:** [SETUP.md](SETUP.md)
- **Full documentation:** [README.md](README.md)
- **Troubleshooting:** [README.md#troubleshooting](README.md#️-troubleshooting)
- **Report bugs:** [GitHub Issues](https://github.com/Paidguy/TelegramRestrictionBypass/issues)

---

## 🚀 What's Next?

Once your bot is running:
- Add more bots: `/connect <token>` for faster downloads
- Set up dump channel: Add bot as admin to a channel
- Try batch download: `/bdl <start_link> <end_link>`
- Explore settings: Click ⚙️ Settings in dashboard

---

**Happy downloading! 📥**
