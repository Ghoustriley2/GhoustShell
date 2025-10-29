import os
from colorama import Fore, init
import time as t
from tqdm import tqdm
import shutil as s

init()

def os_name():
    print(os.name)

def os_system_info():
    os.cpu_count()

def os_system_help():
    print("имя платформы системы: ")
    os_name()
    print("\n")
    print("CPU ядра: ")
    print(os_system_info())
    print("\n")
    print("всё что можно заполучить в этой версии.")

def h():
    cm_list = """
        H or help - помощь по командам
        L or ls - показать текущюю директорию
        M or Mkdir - создать папку в текущей директории
        C or cd - зайти в папку по направлению path
        DD or deldir - удалить папку (пустую)
        RM or remove - удалить файл
        LST or list - посмотреть все файлы в текущей папке
        CP or copy - копировать файл из одного места в другое
        SYS or system - всё что можно получить из инофрмации о вашей системе (beta)
        """
    print(cm_list)

def dd():
    folder_path = input("folder path: ")
    os.rmdir(folder_path)

def l():
    local_path = os.getcwd()
    print(local_path)

def cd():
    path = input("your path to folder: ")
    os.chdir(path)

def m():
    folder_name = input("folder name: ")
    os.mkdir(folder_name)
    print("folder as created.")

def lst():
    local_path = os.getcwd()
    os.listdir(local_path)

def rm():
    file_name = input("file name: ")
    os.remove(file_name)

def cp():
    cp_1 = input("путь файла который нужно скопировать: ")
    cp_2 = input("путь куда вставлять файл: ")
    s.copy2(cp_1, cp_2)

banner_a = '''            ▄▄                                                 ▄▄                  ▄▄    ▄▄'''
banner_b = '''  ▄▄█▀▀▀█▄████                                    ██   ▄█▀▀▀█▄███                ▀███  ▀███'''
banner_c = '''▄██▀     ▀█ ██                                    ██  ▄██    ▀███                  ██    ██'''
banner_d = '''██▀       ▀ ███████▄   ▄██▀██▄▀███  ▀███  ▄██▀████████▀███▄    ███████▄   ▄▄█▀██   ██    ██'''
banner_e = '''██          ██    ██  ██▀   ▀██ ██    ██  ██   ▀▀ ██    ▀█████▄██    ██  ▄█▀   ██  ██    ██'''
banner_g = '''██▄    ▀██████    ██  ██     ██ ██    ██  ▀█████▄ ██  ▄     ▀████    ██  ██▀▀▀▀▀▀  ██    ██'''
banner_h = '''▀██▄     ██ ██    ██  ██▄   ▄██ ██    ██  █▄   ██ ██  ██     ████    ██  ██▄    ▄  ██    ██'''
banner_j = '''▀▀███████████  ████▄ ▀█████▀  ▀████▀███▄██████▀ ▀████▀█████▀████  ████▄ ▀█████▀▄████▄▄████▄'''
banners = [banner_a, banner_b, banner_c, banner_d, banner_e, banner_g, banner_h, banner_j]

line = '---------------------------------------------------------------------------------------------------'

def banner_print():
    for a in banners:
        print(Fore.GREEN + a)
        t.sleep(0.3)
    print(Fore.GREEN + "\n")
    print(Fore.GREEN + line)
    for b in tqdm(range(100), desc=Fore.GREEN + "загрузка", ncols=100):
        t.sleep(0.05)
    print(Fore.GREEN + line)
    t.sleep(3.5)
    os.system("cls")
    print(Fore.GREEN + line)
    tab = "\t"
    print(tab * 5 + Fore.GREEN + "    welcome!")
    print(tab * 5 + Fore.GREEN + " GhoustShell v0.0.1")
    print(Fore.GREEN + line)
    t.sleep(2)

banner_print()

version_info = Fore.GREEN + """
version: v0.0.1 (beta)
price: free
name: GhoustShell
"""

def i():
    print(version_info)

print("\n", version_info)
run = True

while run:
    Cm = input(f"<GhoustLine>: ")
    t.sleep(2)
    if Cm == "H" or Cm == "help":
        h()
    elif Cm == "Info" or Cm == "I" or Cm == "info" or Cm == "INFO":
        i()
    elif Cm == "E" or Cm == "Exit" or Cm == "exit":
        run = False
    elif Cm == "ls" or Cm == "L":
        l()
    elif Cm == "M" or Cm == "mkdir" or Cm == "Mkdir":
        m()
    elif Cm == "dd" or Cm == "DD" or Cm == "deldir":
        dd()
    elif Cm == "cd" or Cm == "Cd" or Cm == "C":
        cd()
    elif Cm == "lst" or Cm == "Lst" or Cm == "list" or Cm == "LST":
        lst()
    elif Cm == "RM" or Cm == "rm" or Cm == "remove":
        rm()
    elif Cm == "CP" or Cm == "cp" or Cm == "Cp" or Cm == "copy":
        cp()
    elif Cm == "Sys" or Cm == "SYS" or Cm == "sys" or Cm == "system":
        os_system_help()
    else:
        print("error")
