#!/usr/bin/env python3
import time #line:3
from colorama import Fore ,Back ,Style ,init #line:4
init (autoreset =True )#line:5
def startMessage ():#line:7
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")#line:8
    OOOO0OO000OO0OOOO ="iloveu"#line:9
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :
        print (Fore .RED +'[X] Wrong Code')
        print (Fore .BLUE +''' 
   1. Go to Insta and massage 
   2. Insta ID: hacker_6_2_9_1
   3. Send massage for code
   4. Next time come with code and use this tool
   5. bye
    ''')#line:18
        startMessage ()#line:19
    else :#line:20
        print (Fore .GREEN +"Successfully Unlocked Tool!")#line:21
        pass #line:22
if __name__ =="__main__":#line:24
    startMessage ()#line:25
    


import smtplib
import socket
import os
import socket


from setup.banner import banner , banner2 , clear
from setup.colors import r,c,g,y,ran
from setup.sprint import sprint


try:
    import socks
except ModuleNotFoundError:
    os.system("pip install spcks")



clear()
banner()
yes = ["y" , "yes"]
no = ["n" , "no"]
print("[ Coded by _.QADIR AHMAD._ ]=")
import urllib.request
import json
ip = input(
    "Just press enter key to get location of your current IP \n OR \n Enter IP address to get its location and other info:"
)

resp = urllib.request.urlopen(
    "http://www.ip-api.com/json/" + ip +
    "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
).read()
resp_dic = json.loads(resp)

print("\n")

for key, value in resp_dic.items():
    print(f"{key} : {value}")
