# handler.py

import time
import psutil
import subprocess
import pyautogui as pg


class cmd():
    print("Write /help!")
    while True:
        command = input("[CMD] " + "Enter your command: ")
        com = command

        commands = ["/help", "/start_players", "/start_admins", "/status"]

        if com == "/help":
            print('''Commands list:        
                     /help - help the commands
                     /start_players - start player server
                     /start_admins - start admin server
                     /status - show machine status                   
        ''')

        if com == "/start_players":
            subprocess.Popen(["start", "cmd"], shell=True).wait()
            time.sleep(2)
            pg.typewrite(f"python Players/PlayerHandler.py")
            pg.press("enter")

        if com == "/start_admins":
            subprocess.Popen(["start", "cmd"], shell=True).wait()
            time.sleep(2)
            pg.typewrite(f"python Admins/AdminHandler.py")
            pg.press("enter")

        if com == "/status":
            print(f"Time - {time.asctime()}\n RAM - {psutil.virtual_memory().percent}%\n CPU - {psutil.cpu_percent()}%\n CPU Count - {psutil.cpu_count()}")

        if com not in commands:
            print("Invalid command!")
            continue
