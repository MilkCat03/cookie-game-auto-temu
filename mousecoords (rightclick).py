import pyautogui
from pynput.mouse import Listener, Button

def on_click(x, y, button, pressed):
    if button == Button.right and pressed:
        print(f"Mouse coordinates: x={x}, y={y}")

# Create a listener object
listener = Listener(on_click=on_click)

# Start the listener
listener.start()

# Keep the script running until interrupted
try:
    listener.join()
except KeyboardInterrupt:
    listener.stop()
