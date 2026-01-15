# Phantom Logger

A cross-platform keylogger written in Python that captures keyboard input and sends formatted logs to a Telegram bot on demand. This tool demonstrates keystroke logging capabilities across Windows, macOS, and Linux systems.

**⚠️ Educational Purpose Only: This tool is designed for cybersecurity education and authorized penetration testing. Unauthorized use of keyloggers is illegal and unethical. Always obtain explicit permission before deploying this software.**

## Telegram Bot Commands
- `/logs`: send log in .txt format
- `/status`: send message to check Phantom Logger status
- `/kill`: destroy Phantom Logger

## Platform-Specific Log Locations

- **Windows**: `%LOCALAPPDATA%\Microsoft\Event Viewer\ExternalLogs.dat`
- **macOS**: `~/Library/Caches/.com.apple.bird.plist`
- **Linux**: `~/.cache/.fontconfig-timestamp.dat`

## Requirements

- Python 3.7+
- Telegram Bot Token (obtain from [@BotFather](https://t.me/botfather))
- Telegram Chat ID

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

## Project Structure
```bash
phantom-logger/
├── main.py                   
├── modules/
│   ├── __init__.py           
│   ├── logger.py             
│   ├── telegram_bot.py       
│   ├── formatter.py          
│   └── utils.py              
├── build.sh                  
├── requirements.txt          
└── .env                                     
```

## Disclaimer
The authors and contributors are not responsible for any misuse of this software. Users assume all legal and ethical responsibility for their actions.