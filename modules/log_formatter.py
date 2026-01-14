import re

class LogFormatter:
    
    @staticmethod
    def format_log(raw_log_path, formatted_log_path):
        try:
            with open(raw_log_path, 'r') as f:
                content = f.read()
            
            formatted = LogFormatter._clean_content(content)
            
            with open(formatted_log_path, 'w') as f:
                f.write(formatted)
                
            return formatted_log_path
            
        except Exception as e:
            return None
    
    @staticmethod
    def _clean_content(content):

        content = re.sub(r'(?<=\S) (?=\S(?= |$))', '', content)

        replacements = {
            'space': ' ',
            'enter': '\n',
            'shift': '',
            'ctrl': '',
            'cmd': '',
            'alt': '',
            'backspace': '[<-]',
            'tab': '\t',
            'caps_lock': '',
            'esc': '[ESC]',
            'delete': '[DEL]',
            'home': '[HOME]',
            'end': '[END]',
            'page_up': '[PGUP]',
            'page_down': '[PGDN]',
            'insert': '[INS]',
            'f1': '[F1]',
            'f2': '[F2]',
            'f3': '[F3]',
            'f4': '[F4]',
            'f5': '[F5]',
            'f6': '[F6]',
            'f7': '[F7]',
            'f8': '[F8]',
            'f9': '[F9]',
            'f10': '[F10]',
            'f11': '[F11]',
            'f12': '[F12]',
        }

        for old, new in replacements.items():
            content = content.replace(old, new)

        content = re.sub(r' +', ' ', content)

        content = re.sub(r'\n{3,}', '\n\n', content)

        lines = [line.strip() for line in content.split('\n')]
        content = '\n'.join(lines)
        
        return content.strip()
