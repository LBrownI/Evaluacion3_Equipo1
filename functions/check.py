from datetime import datetime

# This is an example for the check function using the datatime library
def save_current_action(action: str):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    with open("logs\\logs.txt", "a") as f:
        f.write(f"{time}: {action}\n")
        
def print_logs():
     with open("logs\\logs.txt", "r") as f:
        print(f.read())