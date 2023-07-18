import pyautogui
import keyboard
import sys

image_path = 'Capture.png'

image_found = False

def on_key_press(event):
    if event.name == 'e':
        print("E key pressed. Exiting...")
        global image_found
        image_found = True
        sys.exit(0)

keyboard.on_press(on_key_press)

while not image_found:
    image_location = pyautogui.locateOnScreen(image_path)
    
    if image_location is not None:
        print("Image found!")
        print(f"Image location: {image_location}")
        pyautogui.click(890, 760) # Change this using mousecoords.py

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Program interrupted. Exiting...")

