from datetime import datetime
import getpass

def save_current_action(action: str):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    username = getpass.getuser()
    
    with open("logs\\logs.txt", "a") as f:
        f.write(f"{time} - User: {username} - Action: {action}\n")
        
def print_logs():
     with open("logs\\logs.txt", "r") as f:
        print(f.read())