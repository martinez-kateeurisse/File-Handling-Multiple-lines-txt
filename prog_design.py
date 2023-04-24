#Import colorama
from colorama import Back, Fore, Style 

#Define header design
def multiple_line_header():
    print(Fore.LIGHTRED_EX, """
                                ──────▄▀▄─────▄▀▄
                                ─────▄█░░▀▀▀▀▀░░█▄ 
                                ─▄▄──█░░░░░░░░░░░█──▄▄
                                █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.CYAN,"""  
                   █▀▀ █ █░░ █▀▀ ▄▄ █░█ ▄▀█ █▄░█ █▀▄ █░░ █ █▄░█ █▀▀
                   █▀░ █ █▄▄ ██▄ ░░ █▀█ █▀█ █░▀█ █▄▀ █▄▄ █ █░▀█ █▄█""")
    print(Fore.WHITE,  "="* 25 + "Multiple line text contents file" + "="* 25 ,"\n")