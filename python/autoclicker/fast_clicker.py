import pyautogui
import keyboard
import time

is_clicking = False


def toggle_clicking():
    global is_clicking
    is_clicking = not is_clicking
    if is_clicking:
        print("Clicking started. Press SPACE again to stop.")
    else:
        print("Clicking stopped. Press SPACE again to start.")


# Set a hotkey for spacebar to toggle clicking
keyboard.add_hotkey("space", toggle_clicking)

print("Press SPACE to start clicking...")

try:
    while True:
        if is_clicking:
            pyautogui.click()
            # Adjust the speed here; smaller delay = faster clicking
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Exiting script.")
