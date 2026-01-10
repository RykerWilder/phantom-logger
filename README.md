# Phantom Logger

A cross-platform keylogger written in Python that captures keyboard input and stores it in hidden system directories. This tool demonstrates keystroke logging capabilities across Windows, macOS, and Linux systems.

⚠️ Educational Purpose Only: This tool is designed for cybersecurity education and authorized penetration testing. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit permission before deploying this software.

## Platform-Specific Log Locations

Windows: %LOCALAPPDATA%\Microsoft\Event Viewer\ExternalLogs.dat

macOS: ~/Library/Caches/.com.apple.bird.plist

Linux: ~/.cache/.fontconfig-timestamp.dat


## Requirements
- Python 3.x

## Installation

1. Clone repository
```bash
git clone https://github.com/RykerWilder/phantom-logger
```

2. Enter directory
```bash
cd phantom-logger
```

3. Create virtual environment and activate it
```bash
python3 -m venv venv

source venv/bin/activate
```

4. Install dependencies
```bash
pip3 install -r requirements.txt
```

## Disclaimer
The authors and contributors are not responsible for any misuse of this software. Users assume all legal and ethical responsibility for their actions.