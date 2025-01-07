import pyautogui
import keyboard

is_clicking = False


def toggle_clicking():
    global is_clicking
    is_clicking = not is_clicking
    if is_clicking:
        print("Clicking started. Press SPACE again to stop.")
    else:
        print("Clicking stopped. Press SPACE again to start.")


keyboard.add_hotkey("space", toggle_clicking)

print("Press SPACE to start clicking...")

try:
    while True:
        if is_clicking:
            pyautogui.click()
            # Removed the sleep to click as fast as Python can handle
except KeyboardInterrupt:
    print("Exiting script.")
