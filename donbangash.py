#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By RANA MZ.
#################################################################
#         		ATHOUR : ISHTIAQ KHAN			#
#  		     NAM TU SUNA HUGA			#
#################################################################
#By RanaMZ
 
import os, sys, time, datetime, re, threading, json, random, requests, hashlib, cookielib, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('clear')
logo = """
   
  .d8888b.   .d88888b.  888b     d888        d8888 8888888 888      
d88P  Y88b d88P" "Y88b 8888b   d8888       d88888   888   888      
Y88b.      888     888 88888b.d88888      d88P888   888   888      
 "Y888b.   888     888 888Y88888P888     d88P 888   888   888      
    "Y88b. 888     888 888 Y888P 888    d88P  888   888   888      
      "888 888     888 888  Y8P  888   d88P   888   888   888      
Y88b  d88P Y88b. .d88P 888   "   888  d8888888888   888   888      
 "Y8888P"   "Y88888P"  888       888 d88P     888 8888888 88888888 
                      
=============================                                       
## ATHOUR .ISHTIAQ KHAN
#############################
## BRAND  : ISHTIAQ-BRAND
## FACEBOOK : MUHAMMAD
## YOUTUBE  : TECH ISHTOO
## TOOL TYPE : PAID 350 RS
## CREATE BY : MUHAMMAD ISHTIAQ
## SOLO : TEAM
## FREE : WALA DOOR RAHOO
## UPDATE : 11 April 2020
## VERSION : 2.0.0
"""
 
 
def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;32;1m WELCOME TO THE SOMAIL-BRAND NEW UPDATE TOOLS ....!'
    print ''
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/bin/.gshsh-cov', 'r').read()
    except (KeyError, IOError):
    	reg2()
 
    r = requests.get('https://raw.githubusercontent.com/ZX3704/somail/main/Somail.txt').text
    if to in r:
        ip()
    else:
        os.system('clear')
        print logo
        print '\tN O T       WELCOME   ....!'
        print '+=========================================+ '
        print '\x1b[1;97m N O T E  : CREATE BY SOMAIL'
        print '\x1b[1;97m  OKZ IDZ COMING INSHALLAH'
        print '\x1b[1;97m           O N E R  : SOMAIL-BRAND '
        print '+=========================================+ '
        print ' \x1b[1;97m Y O U R    T O K E N : ' + to
        raw_input('\x1b[1;92m      E N T E R GO TO WHATSAPP   ')
        os.system('xdg-open https://wa.me/03449843934?text=Assalamualaikum Sir Approve my Token and my Token :'+id)
        reg()
 
 
def reg2():
    os.system('clear')
    print logo
    print '\tN O T    OK....!'
    print ' \x1b[1;92m Copy and press enter , then select Facebook to continue'
    id = uuid.uuid4().hex[:10]
    print ' YOUR TOKEN : ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923185612237?text=Assalamualaikum Sir Approve my Token and my Token :'+id)
    sav = open('/data/data/com.termux/files/usr/bin/.gshsh-cov', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;97m    GO TO WHATSAPP')
    reg()
    
    
 
def ip():
    os.system('clear')
    print logo
    print '\tP L E A S E     W A I T...!'
    try:
        ipinfo = requests.get('http://IP-API.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass
        
    print ' +==========================+'
    print '\x1b[1;97m YOUR IP: ' + ips
    time.sleep(1)
    print '\x1b[1;97m YOUR COUNTRY: ' + country
    time.sleep(1)
    print '\x1b[1;97m YOUR REGION: ' + regi
    os.system('clear')
    print logo
    print 47 * '-'
    print ' +=========================================+'
    print '\x1b[1;92m[1] \x1b[1;97m | GO TO MEN MENU'
    print ' +========================================+'
    menu_s()
 
 
def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80\xe2\x9e\xa4 ')
    if ms == '1':
    	os.system("rm -rf $HOME/Zbqjab")
    	os.system("cd $HOME && git clone https://github.com/ZX3704/Zbqjab && cd Zbqjab && python SOMAIL-BRAND.py")
        os.system('xdg-open https://wa.me/+923185612237?text=Assalamualaikum Sir Approve my Token and my Token :'+id)
    else:
        print ''
        print '\tSELECT VALID OPITION'
        print ''
        menu_s()
 
 
if __name__ == '__main__':
    reg()
