import keyboard
from colorama import Fore,Back,Style,just_fix_windows_console
from time import sleep
import os

just_fix_windows_console()

clear = lambda: os.system("cls")

def highlight(text:str)->str:
    return Fore.BLACK + Back.WHITE + text + Style.RESET_ALL

def menu_display(menu:dict):
    selected_option=0
    while True:
        clear()
        for id,option in enumerate(menu):
            if id==selected_option:
                option=highlight(option)
            print(option)
        sleep(0.1)
        key=None
        while not key:
            key=keyboard.read_key()
            if key=='up': selected_option-=1
            elif key=='down': selected_option+=1
            elif key=='enter': return list(menu.values())[selected_option]()
            elif key=='esc': return
            else: key=None
            selected_option%=len(menu)

def menu():
    menu_dict={}
    menu_display(menu_dict)


if __name__=='__main__':
    menu()



