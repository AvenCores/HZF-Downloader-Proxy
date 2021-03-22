import os
import requests

def ProxyScape():
    global banner
    menu = input(banner + '\n1 - Скачать HTTP Proxy\n2 - Скачать Socks4 Proxy\n3 - Скачать Socks5 Proxy\n\n0 - Вернуться в главное меню\n')
    if menu == "0": return()
    if menu == "1": httpDW()
    if menu == "2": socks4DW()
    if menu == "3": socks5DW()

def httpDW():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScape_http_proxies.txt', "wb")
    ufr = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nHTTP Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def socks4DW():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScape_socks4_proxies.txt', "wb")
    ufr = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nSocks4 Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def socks5DW():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScape_socks5_proxies.txt', "wb")
    ufr = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nSocks5 Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def ProxyScan():
    menu = input(banner + '\n1 - Скачать HTTP Proxy\n2 - Скачать HTTPS Proxy\n3 - Скачать Socks4 Proxy\n4 - Скачать Socks5 Proxy\n\n0 - Вернуться в главное меню\n')
    if menu == "1": httpDWScan()
    if menu == "2": httpsDWScan()
    if menu == "3": socks4DWScan()
    if menu == "4": socks5DWScan()

def httpDWScan():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScan_HTTP_proxies.txt', "wb")
    ufr = requests.get("https://www.proxyscan.io/download?type=http")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nHTTP Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def httpsDWScan():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScan_HTTPS_proxies.txt', "wb")
    ufr = requests.get("https://www.proxyscan.io/download?type=https")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nHTTPS Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def socks4DWScan():
    path = 'c:/HZF ProxyList/'
    try:
        os.mkdir(path)
    except OSError as error:
        False
    os.system('cls')

    f=open(r'c:/HZF ProxyList/ProxyScan_SOCKS4_proxies.txt', "wb")
    ufr = requests.get("https://www.proxyscan.io/download?type=socks4")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nSocks4 Proxy List был скачен в папку C:/HZF ProxyList/\n\n\nНажмите ENTER для выхода в главное меню")
    input()

def socks5DWScan():
    mkdir = 'c:/HZF ProxyList/'
    system('cls')
    f=open(r'c:/HZF ProxyList/ProxyScan_SOCKS5_proxies.txt', "wb")
    ufr = requests.get("https://www.proxyscan.io/download?type=socks5")
    f.write(ufr.content)
    f.close()
    global banner
    print(banner+"\nSocks5 Proxy List был скачен в папку C:/HZF ProxyList/\n\nНажмите ENTER для выхода в главное меню")
    input()

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nЗа все действия с программой отвечаете только вы!\n\nСоздатель Telegram - @avencores\n\nНажмите ENTER чтобы выйти")
    input()

while True:
    banner = ("\n" * 100)+ """
 ______        __  ____
|  _ \ \      / / |  _ \ _ __ _____  ___   _
| | | \ \ /\ / /  | |_) | '__/ _ \ \/ / | | |
| |_| |\ V  V /   |  __/| | | (_) >  <| |_| |
|____/  \_/\_/    |_|   |_|  \___/_/\_\\__, |
                                       |___/
Telegram Channel: t.me/hzfnews
VK: vk.com/hzforum1
    """

    print(banner)
    menu = input('1 - ProxyScape - HTTP/Socks4/Socks5\n2 - ProxyScan - HTTP/HTTPS/Socks4/Socks5\n\n3 - Важная информация\n\n0 - Выход\n')
    if menu == "0": exit()
    if menu == "1": ProxyScape()
    if menu == "2": ProxyScan()
    if menu == "3": info()
