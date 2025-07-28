taskkill /f /im python.exe /fi "WINDOWTITLE eq start.py"

:: Wait a moment for cleanup
timeout /t 2

:: Start the task again
schtasks /run /tn "startbot"
