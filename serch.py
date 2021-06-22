import os
import subprocess
import random
import time

serch_ip = 0
serch_ip = input()
print(serch_ip)

os.system("ping -c 10 %s" %(serch_ip))
os.system('nmap %s' %(serch_ip))