import platform
import os

def get_log_path():
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Event Viewer', 'ExternalLogs.dat')
        
    elif system == "Darwin":
        return os.path.expanduser('~/Library/Caches/.com.apple.bird.plist')
        
    elif system == "Linux":
        return os.path.expanduser('~/.cache/.fontconfig-timestamp.dat')
