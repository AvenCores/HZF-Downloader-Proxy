from os import system,mkdir,name
from requests import get
from termcolor import colored
from pathlib import Path
from sys import platform

version = 1.1

def ProxyScape():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    global banner6
    menu = input(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + colored("1 ", "cyan") + "- Скачать HTTP Proxy\n" + colored("2 ", "cyan") + "- Скачать Socks4 Proxy\n" + colored("3 ", "cyan") + "- Скачать Socks5 Proxy\n\n" + colored("0 ", "cyan") + "- Вернуться в главное меню\n")
    if menu == "0": return()
    if menu == "1": httpDW()
    if menu == "2": socks4DW()
    if menu == "3": socks5DW()

def httpDW():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScape_http_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTP Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScape_http_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTP Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def socks4DW():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScape_socks4_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSocks4 Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScape_socks4_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSocks4 Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def socks5DW():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScape_socks5_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSocks5 Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScape_socks5_proxies.txt', "wb")
        ufr = get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSocks5 Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def ProxyScan():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    global banner6
    menu = input(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + colored("1 ", "cyan") + "- Скачать HTTP Proxy\n" + colored("2 ", "cyan") + "- Скачать HTTPS Proxy\n" + colored("3 ", "cyan") + "- Скачать Socks4 Proxy\n" + colored("4 ", "cyan") + "- Скачать Socks5 Proxy\n\n" + colored("0 ", "cyan") + "- Вернуться в главное меню\n")
    if menu == "0": return()
    if menu == "1": httpDWScan()
    if menu == "2": httpsDWScan()
    if menu == "3": socks4DWScan()
    if menu == "4": socks5DWScan()

def httpDWScan():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScan_HTTP_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=http")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTP Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScan_HTTP_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=http")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTP Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def httpsDWScan():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScan_HTTPS_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=https")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTPS Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScan_HTTPS_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=https")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nHTTPS Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def socks4DWScan():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScan_SOCKS4_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=socks4")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSOCKS4 Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScan_SOCKS4_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=socks4")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSOCKS4 Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def socks5DWScan():
    if platform == "linux" or platform == "linux2" or platform == "unix":
        Path("HZF ProxyList").mkdir(parents=True, exist_ok=True)
        system('cls' if name == 'nt' else 'clear')
        f=open(r'HZF ProxyList/ProxyScan_SOCKS5_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=socks5")
        f.write(ufr.content)
        f.close()
        system("mv HZF\ ProxyList $HOME")
        global banner
        global banner2
        global banner3
        global banner4
        global banner5
        global banner6
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSOCKS5 Proxy List был загружен в папку $HOME/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

    elif platform == "win32":
        path = 'c:/HZF ProxyList/'
        try:
            mkdir(path)
        except OSError as error:
            False
        system('cls' if name == 'nt' else 'clear')
        f=open(r'c:/HZF ProxyList/ProxyScan_SOCKS5_proxies.txt', "wb")
        ufr = get("https://www.proxyscan.io/download?type=socks5")
        f.write(ufr.content)
        f.close()
        print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nSOCKS5 Proxy List был загружен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
        input()

def info():
    global banner
    global banner2
    global banner3
    global banner4
    global banner5
    global banner6
    print(banner + "\n" + banner2 + "\n" + banner3 + "\n" + banner4 + "\n" + banner5 + "\n" + banner6 + "\n" + "\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @hzfnews\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100) + colored("""
██████╗ ██╗    ██╗    ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗██║    ██║    ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
██║  ██║██║ █╗ ██║    ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ 
██║  ██║██║███╗██║    ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  
██████╔╝╚███╔███╔╝    ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║  
    """, "green")
    banner2 = colored("[", "blue")+"Developers      :"+colored("HZF", "green")
    banner3 = colored("[", "blue")+"Version         :"+colored(version, "red")
    banner4 = colored("[", "blue")+"Telegram Channel:"+colored("@hzfnews", "cyan")+colored("              <-- Подпишись!", "green")
    banner5 = colored("[", "blue")+"YouTube Channel :"+colored("youtube.com/c/HZFYT", "cyan")+colored("   <-- Подпишись!", "green")
    banner6 = colored("[", "blue")+"VK              :"+colored("vk.com/hzforum1", "cyan")+colored("       <-- Подпишись!", "green")+"\n"

    print(banner)
    print(banner2)
    print(banner3)
    print(banner4)
    print(banner5)
    print(banner6)
    menu = input(colored("1 ", "cyan") + "- ProxyScape - HTTP/Socks4/Socks5\n" + colored("2 ", "cyan") +  "- ProxyScan - HTTP/HTTPS/Socks4/Socks5\n\n" + colored("99 ", "cyan") + "- Важная информация\n\n" + colored("0 ", "cyan") +  "- Выход\n")
    if menu == "1": ProxyScape()
    if menu == "2": ProxyScan()
    if menu == "99": info()
    if menu == "0": exit()