import subprocess
import psutil
from config import CSLOL_PATH, USER_ID

async def handle_presence_update(before, after):
    if after.id != USER_ID:
        return

    for activity in after.activities:
        if activity.type.name.lower() == "playing" and "League of Legends" in activity.name:
            if not is_process_running("cslol-manager"):
                subprocess.Popen([CSLOL_PATH])
            break

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False