import colorama
import pathlib
import sys

colorama.init(autoreset=True)

path = sys.argv[1]

def listdir(path, tab=0):
    p = pathlib.Path(path)
    lst = p.iterdir()
    for el in lst:
        if el.is_dir():
            print(colorama.Fore.GREEN+(tab*' ')+'\\'+el.name)
            listdir(el, tab+1)
        else:
            print(colorama.Fore.LIGHTYELLOW_EX+(tab*' ')+'|'+el.name)

listdir(path)