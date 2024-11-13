#/usr/bin/python 3.12.6
#liberary & Module Reqaired
#Port Scanner Developed by cyb3rs3m //https://t.me/mk3em https://t.me/hakfateam

import socket
import subprocess
import sys
import pyfiglet #pip install pyfiglet
import sys
import colorama #pip install colorama
colorama.init()
from loaders import TextLoader #pip install pyloaders For Install Package
                                          

#this is banner for start script with pyfiglet repository

asci_banner = pyfiglet.figlet_format(colorama.Fore.YELLOW + "SCanNer")
print (colorama.Fore.LIGHTRED_EX + """Please Loading For Script""")

print("""Welcome To Suitescript From Hackfateam
https://t.me/hakfateam""")

print(colorama.Fore.LIGHTWHITE_EX + "#" * 60)

#webanner = pyfiglet.figlet_format("hakfateam")

print(colorama.Fore.CYAN + asci_banner)

#print(webanner)

from datetime import datetime

subprocess.call('clear', shell=True) # for run command prompt (cmd) in windows and clear text screen

print(colorama.Fore.LIGHTWHITE_EX + "#" * 60)

remoteServer = input(colorama.Fore.GREEN + "Please Enter Target Host To Scan: ")

IP_back = socket.gethostbyname(remoteServer)

print ( "_" * 60)

#print (fixed_loader)

#part of loading script when start scan 

fixed_loader = TextLoader(duration=12)
fixed_loader.run() # Pauses program execution and runs loader for 10s

loader2 = TextLoader(animation='loop')
loader2.run()

print ("_" * 60)

b1 = datetime.now()

try:

    for port in range(1 , 1000): #Range Port For Scanning your Can Change It :)
        
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        
        result = sock.connect_ex((remoteServer,port))
        
        if result == 0:
          
            print("port {} Is Open".format(port)) 
          
            sock.close()

except KeyboardInterrupt:
    
    print (colorama.Fore.RED + "You pressed Ctrl+C")

sys.exit()

#HERE IS SCRIPT FINISH #


