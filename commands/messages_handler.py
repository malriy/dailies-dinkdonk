import pyautogui
import subprocess
import traceback
import asyncio
import events.presence_handler
from config import EXE_PATHS, IMAGE_PATHS

# Function to handle messages from user
async def handle_message(message):
    if message.author.bot:
        return

    if message.content.startswith('hello'):
        await message.channel.send("Hello! :D")

    if message.content.startswith('!hsr'):
        await message.channel.send("Starting Star Rail...")
        await click_until_stop(EXE_PATHS["hsr"], "StarRail.exe", IMAGE_PATHS["hsr"])    

    if message.content.startswith('!genshin'):
        await message.channel.send("Starting Genshin...")
        await click_until_stop(EXE_PATHS["genshin"], "GenshinImpact.exe", IMAGE_PATHS["genshin"])

    if message.content.startswith('!browser'):
        await message.channel.send("Starting Opera...")
        subprocess.Popen([EXE_PATHS["opera"]])

# Function to click on HSR/Genshin until it fully logs in
async def click_until_stop(path, game,stopimg):
    try:
        pyautogui.hotkey('win', 'd')
        subprocess.Popen([path])
        await asyncio.sleep(45)
        pyautogui.moveTo(960, 540, duration=0.8)

        while events.presence_handler.is_process_running(game):
            try:
                stop = pyautogui.locateOnScreen(stopimg, confidence=0.7)
            except pyautogui.ImageNotFoundException:
                stop = None

            if stop:
                print(f"Found image. Stopping click.")
                break
            else:
                
                pyautogui.click()
                await asyncio.sleep(15)

        print(f"Game stopped")

    except Exception as e:
        print(f"Error launching game: {e}")
        traceback.print_exc()