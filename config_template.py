import os

# ------------------------------
# Discord Bot Configuration
# ------------------------------
TOKEN = "YOUR_DISCORD_BOT_TOKEN"  # Replace with your actual bot token

# ------------------------------
# Game Executable Paths
# ------------------------------
CSLOL_PATH = r"PATH\TO\cslol-manager.exe"
GENSHIN_PATH = r"PATH\TO\GenshinImpact.exe"
HSR_PATH = r"PATH\TO\StarRail.exe"

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
