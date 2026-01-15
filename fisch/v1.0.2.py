import keyboard
from datetime import datetime

def print_time():
    print(datetime.now().strftime("%H:%M:%S"))

keyboard.add_hotkey("g", print_time)

keyboard.wait()
