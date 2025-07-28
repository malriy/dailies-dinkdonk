# Dailies DinkDonk

Simple mini project to automate launching and interacting with games using Discord bot commands and image recognition via PyAutoGUI.

---

## ⚙️ Features

- Launch games via Discord commands (`!hsr`, `!genshin`)
- Detect when games are running to avoid duplicate launches
- Does image-based screen detection using `.png` templates
- Tracks your Discord presence to trigger actions based on your activity

---

## 🧱 Project Structure

```
DailiesBot/
├── bot.py                  # Launches the Discord client
├── config.py               # User-specific configuration (gitignored)
├── config_template.py      # Sample config file for reference
├── commands/
│   └── message_handler.py  # Handles Discord message-based commands
├── events/
│   └── presence_handler.py # Tracks Discord presence and game activity
├── images/                 # Folder with UI templates (.png)
└── README.md
```

---

## 📝 Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/dailies-dinkdonk.git
   cd dailies-dinkdonk
   ```

2. **Install dependencies**

   If you're doing image recognition:

   ```bash
   pip install pyautogui opencv-python psutil Pillow
   ```

3. **Create your config file**

   - Copy `config_template.py` → `config.py`
   - Fill in bot `TOKEN`, local *(absolute)* paths to executables, user ID, and image filenames.

4. **Prepare image templates**

   - Place UI button screenshots in `images/` (e.g. `hsrui.png`, `genshinui.png`)

5. **Ignore sensitive info** Make sure `config.py` is listed in your `.gitignore`:

   ```
   config.py
   ```

---

## ▶️ Starting the Bot

### Manual launch via .bat file

```bash
@echo off
cd path/to/DailiesBot
python bot.py
pause
```

✅ The terminal should show:

```
Logged in as YourBotName#1234
```

### To make life easier, make a .vbs script to launch the .bat file with no CMD window and put in task scheduler
```
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "Path:\to\batFile\start.bat" & Chr(34), 0
Set WshShell = Nothing
```
---

## 💬 Usage (Discord Commands)

| Command    | Description                                             |
| ---------- | ------------------------------------------------------- |
| `!hsr`     | Launches Star Rail and clicks stop image until UI shown |
| `!genshin` | Launches Genshin and clicks stop image until UI shown   |
| `hello`    | Test command; bot replies “Hello! :D”                  |

---

## 🧹 Other Behavior

My own thing: the bot will **watch Discord presence**. When you start playing League of Legends, it launches my third-party tool (`cslol-manager` LoL mods), unless it's already running.

---

## 🛠 Troubleshooting Tips

- **Bot never shows online?**

  - Ensure `config.py` has the correct token.
  - Confirm you're running the bot script, not just `bot.py` in a different directory.
  - Wanted privileged intents? Enable `message_content`, `presences`, and `members` in Developer Portal.

- **Image recognition not working?**

  - Make sure your screenshot resolution matches runtime resolution.
  - Install `opencv-python` to use `confidence=` parameter in `locateOnScreen`.
  - Adjust confidence (e.g., `0.8 → 0.7`) if match fails.

- **Command triggers multiple launches?**

  - Check that your `is_process_running()` function uses correct `.exe` name.
  - Add locks or prevent multi-instance launch logic.

---


