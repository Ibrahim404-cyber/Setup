#Semple setup script
#open source
#pro ingor
#user use.....

import os
import sys
import time
from os import system as Ibrahim

Ibrahim("clear")
logo=("""\033[1;37m              
\033[1;97m═════════════════════════════════════════════
[\033[1;92m🔥\033[1;97m]OWNER          \033[1;91m: \033[1;97mIbrahim404-Cyber
[\033[1;92m🔥\033[1;97m]TOOL           \033[1;91m: \033[1;97mTERMUX SET-UP 
[\033[1;92m🔥\033[1;97m]VERSION        \033[1;91m: \033[38;5;208mBETA 
\033[1;97m═════════════════════════════════════════════ """)

def Ibrahim_menu():
    Ibrahim('clear')
    print(logo)
    print('\033[1;97m[\033[1;92m1\033[1;97m] TERMUX BASIC-SETUP   \033[1;92m[BEST]')
    print('\033[1;97m[\033[1;92m2\033[1;97m] TERMUX FULL-SETUP  \033[1;92m[Excellent]')
    print('\033[1;97m[\033[1;92m3\033[1;97m] CONTRACT ADMIN \033[1;92m[REPORT A PROBLEM]')
    print('\033[1;97m══════════════════════════════════════════════')
    print('\033[1;97m[\033[1;91m0\033[1;97m] Exit')
    print('\x1b[91m══════════════════════════════════════════════')
    opt = input('\x1b[92mChoose option: \x1b[97m')
    if opt =='1':
        basic_setup()
    if opt =='2':
        print("\n\033[1;92mTermux Does Not Require Complete Set-up");time.sleep(2)
        print("\033[1;97mUse Basic Set-up....");time.sleep(1)
        print("\n\033[1;92mContact admin for more information")
        Ibrahim('xdg-open https://www.facebook.com/shifat.ff.buy.sell?mibextid=ZbWKwL');time.sleep(3)
        Ibrahim_menu()
    if opt =='3':
        Ibrahim_admin()
    elif opt =='0':
        exit()
    else:
        print('\n\x1b[91mCHOOSE VALID OPTION\033[0;97m');time.sleep(1)
        Ibrahim_menu()
        
def basic_setup():
	
  Ibrahim("termux-setup-storage")
  Ibrahim("apt update")
  Ibrahim("apt upgrade -y")
  Ibrahim("pkg install python2 -y")
  Ibrahim("pkg install python3 -y")
  Ibrahim("pkg install git")
  Ibrahim("pip install requests")
  Ibrahim("pip install bs4")
  Ibrahim("pip install mechanize")
  Ibrahim("pip install rich")
  Ibrahim("pip2 install requests -y")
  Ibrahim("pkg install bash -y")
  Ibrahim("pkg install nano -y")
  Ibrahim("pkg install php -y")
  Ibrahim("pip install future -y")
  Ibrahim("pip install requirements -y")
  Ibrahim("pip install httpx")
  print('\033[1;92mYour Termux Set-up Complete')
     
 
 
def Ibrahim_admin():
    Ibrahim('clear')
    print(logo)
    print('\033[1;97m[\033[1;92m1\033[1;97m] Contract WhatsApp ')
    print('\033[1;97m[\033[1;92m2\033[1;97m] Follow Facebook ')
    print('\033[1;97m[\033[1;92m3\033[1;97m] Follow Github')
    print('\033[1;97m[\033[1;91m0\033[1;97m] Back Menu')
    print('\x1b[91m══════════════════════════════════════════════')
    admin_s_x = input('\x1b[92mChoose option: \x1b[97m')
    if admin_s_x =='1':
        Ibrahim('xdg-open https://wa.me/+8801880322043');time.sleep(1)
        Ibrahim_admin()
    if admin_s_x =='2':
        Ibrahim('xdg-open https://www.facebook.com/ibrahim.kholi.ullah2');time.sleep(1)
        Ibrahim_admin()
    if admin_s_x =='3':
        Ibrahim('xdg-open https://github.com/Ibrahim404-cyber')
        Ibrahim_admin()
    if admin_s_x =='0':
        Ibrahim_menu()


Ibrahim_menu()


#""'pkg install git #pkg install python #rm -rf Termux_Set-up #git clone https://github.com/SIFAT-XD/Termux_Set-up #cd Termux_Set-up #python Termux_Set-up.py""'