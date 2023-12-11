from datetime import datetime
import getpass, os

def save_current_action(action: str):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    username = getpass.getuser()
    
    with open("logs\\logs.txt", "a") as f:
        f.write(f"{time} - User: {username} - Action: {action}\n")
        
def print_logs():
    if os.name == 'nt':
        import msvcrt

    def display_text(lines, start_line, num_lines):
        for i in range(start_line, min(start_line + num_lines, len(lines))):
            print(lines[i].rstrip())

    def get_user_input():
        if os.name == 'nt':
            key = msvcrt.getch()
            return key
        else:
            user_input = input("Press 'q' to exit the mode. + to move up. - to move down: ")
            return user_input

    def show_logs():
        with open('logs\\logs.txt', 'r') as file:
            lines = file.readlines()

        start_line = len(lines) - 1
        num_lines_displayed = 14

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            display_text(lines, start_line, num_lines_displayed)

            print("Press 'q' to exit the mode. '+' to move up. '-' to move down")
            key = get_user_input()

            if key == b'+' and start_line > 0:
                start_line -= 1
            elif key == b'-' and start_line < len(lines) - num_lines_displayed:
                start_line += 1
            elif key.lower() == b'q':
                break

    show_logs()
