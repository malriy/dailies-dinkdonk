import os

# ------------------------------
# Discord Bot Configuration
# ------------------------------
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your actual bot token

# ------------------------------
# Game Executable Paths
# ------------------------------
EXE_PATHS = {
    "appName": r"PATH:\To\App",
    "appName": r"PATH:\To\AnotherApp"
}

# ------------------------------
# Discord User ID to Track (Optional)
# ------------------------------
USER_ID = 123456789012345678  # Replace with your user ID

# ------------------------------
# Image Paths for UI Detection
# ------------------------------
IMAGE_DIR = "images"

IMAGE_PATHS = {
    "hsr": os.path.join(IMAGE_DIR, "hsrui.png"),
    "genshin": os.path.join(IMAGE_DIR, "genshinui.png"),
}
