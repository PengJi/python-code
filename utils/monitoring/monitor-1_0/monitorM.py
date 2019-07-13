#!/usr/bin/env python

import os
import sys
import time
import paramiko
import threading
from colorama import Fore, Back, Style

# connect ssh hosts and execute commands
def ssh2(ip,username,passwd,cmd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip,22,username,passwd,timeout=5)
		for m in cmd:
			stdin, stdout, stderr = ssh.exec_command(m)
			#stdin.write("Y")  # simple interaction, enter 'Y'
			'''
			out = stdout.readlines()
			for o in out:
				print o,
			'''
		print Fore.GREEN + '%s\tOK\n'%(ip)
	except:
		print Fore.RED + '%s\tError\n'%(ip)
	finally:
		ssh.close()
		print Style.RESET_ALL


if __name__ == '__main__':
	username = "scidb"  # username
	passwd = "scidb"    # password
	threads = []   # multi-thread

	# 1.create array
	print "create array"
	
	print Fore.GREEN + "monitoring process of loading data"

	# 2.monitoring
	cmd = ['python /tmp/monitorS.py &']  # commands lists
	for i in range(71,78):
		ip = '192.168.100.'+str(i)
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()

	# 3.load data imitation
	time.sleep(5)	

	# 4.end monitoring
	cmd = ['pgrep python | xargs kill -9']  # commands lists
	for i in range(72,78):
		ip = '192.168.100.'+str(i)
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()

	# let above threads completely execte
	time.sleep(3)

	print Fore.YELLOW + "monitoring process of loading data"
	
	# 5.monitoring
	cmd = ['python /tmp/monitorS.py &']  
	for i in range(71,78):
		ip = '192.168.100.'+str(i)
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()

	# 6.query imitation
	time.sleep(5)	

	# 7.end monitoring
	cmd = ['pgrep python | xargs kill -9'] 
	for i in range(72,78):
		ip = '192.168.100.'+str(i)
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()
	

	print Fore.RED + "execute python done"
	print Style.RESET_ALL
