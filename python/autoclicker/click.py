import pyautogui
import keyboard
import time
import threading
import sys


class Clicker:
    def __init__(self):
        self.clicking = False
        self.running = True  # To handle program exit
        keyboard.add_hotkey("space", self.toggle_clicking)  # Toggle clicking with space
        keyboard.add_hotkey("esc", self.stop_program)  # Stop program with ESC
        print("Press space to start/stop clicking. Press ESC to quit.")

    def toggle_clicking(self):
        self.clicking = not self.clicking

    def stop_program(self):
        print("Stopping program...")
        self.running = False  # Set running to False to stop the loop

    def run(self):
        try:
            while self.running:
                if self.clicking:
                    pyautogui.click()  # This clicks the mouse
                    time.sleep(0.0001)  # Adjust this for clicking speed
                else:
                    time.sleep(0.0001)  # Avoid busy waiting
        except KeyboardInterrupt:
            self.stop_program()


if __name__ == "__main__":
    clicker = Clicker()

    # Run the clicker in a separate thread to listen for keyboard input without blocking
    clicker_thread = threading.Thread(target=clicker.run)
    clicker_thread.start()

    # Keep the main thread alive to listen for keyboard inputs
    clicker_thread.join()  # Wait for the clicker thread to finish before exiting
