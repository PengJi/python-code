#!/usr/bin/env python

import os
import sys
import time
import paramiko
import threading
from colorama import Fore, Back, Style

STATS = []

# monitoring CPU
def cpuinfo():
    lines = open('/proc/stat').readlines()
    for line in lines:
        ln = line.split()
        if ln[0].startswith('cpu'):
            return ln;
    return []

# monitoring mem
def Memory():
    mem = {}
    lines = open('/proc/meminfo').readlines()
    for line in lines:
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = float(var)
    STATS[0:] = [mem['MemTotal']]
    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    STATS[1:] = [mem['MemUsed']]
    u = round((mem['MemUsed'])/(mem['MemTotal']),5)
    STATS.append('%.2f%%'%(u*100))

# monitoring disk

def disk_stat():
    import os
    hd={}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail/(1024*1024*1024)
    hd['capacity'] = disk.f_bsize * disk.f_blocks/(1024*1024*1024)
    hd['used'] = disk.f_bsize * disk.f_bfree/(1024*1024*1024)
    return hd

# monitoring net
def rx():
	ifstat = open('/proc/net/dev').readlines()
	for interface in  ifstat:
		if INTERFACE in interface:
			stat = float(interface.split(":")[1].split()[0])
			STATS[0:] = [stat]

def tx():
	ifstat = open('/proc/net/dev').readlines()
	for interface in  ifstat:
		if INTERFACE in interface:
			stat = float(interface.split()[9])
			STATS[1:] = [stat]

def net_stat():
	print 'In   Out'
	rx()
	tx()

# connect remote hosts and execute commands
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
	print Fore.BLUE + "CPU_per"
	# execte once
	W = cpuinfo()
	one_cpuTotal=long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])
	one_cpuused=long(W[1])+long(W[2])+long(W[3])
	# loop execution
	'''
	while True:
		time.sleep(2)
        W = cpuinfo()
        two_cpuTotal=long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])
        two_cpuused=long(W[1])+long(W[2])+long(W[3])
        cpuused=float(two_cpuused-one_cpuused)/(two_cpuTotal-one_cpuTotal)
        print '%.2f%%'%(cpuused*100)
	'''

	print Fore.CYAN + "mem monitoring"
	try:
		print 'Memory_Total      Memory_Used        Used_Per' 
		'''
		while True:
			time.sleep(1)
			Memory()
			MemT = STATS[0]
			MemU = STATS[1]
			Used_Per = STATS[2]
			print MemT ,'KB     ',MemU ,'KB       ',Used_Per  
		'''
	except KeyboardInterrupt, e:
		print "\nmemmonit exited"

	print Fore.YELLOW + "IO monitoring"

	print Fore.MAGENTA + "net monitoring"
	'''
	while True:
		time.sleep(1)
		rxstat_o = list(STATS)
		rx()
		tx()
		RX = float(STATS[0])
		RX_O = rxstat_o[0]
		TX = float(STATS[1])
		TX_O = rxstat_o[1]
		RX_RATE = round((RX - RX_O)/1024,3)
		TX_RATE = round((TX - TX_O)/1024,3)
		print RX_RATE ,'KB  ',TX_RATE ,'KB'
	'''

	cmd = ['glances --export-csv /tmp/glances.csv -t 0.5;hostname > /tmp/hostname.txt']  # commands lists
	username = "scidb"  # username
	passwd = "scidb"    # password
	threads = []   # multi-thread
	print Fore.WHITE
	print "Begin......"

	# create array
	os.system("echo 'create array'")
	
	# load data
	#cmd = ['glances -t 0.5 --export-csv /tmp/glances.csv','hostname']  # commands lists
	#cmd = ['glances --export-csv /tmp/glances.csv -t 0.5;sleep 2','sudo pgrep glances | xargs kill -9']  # commands lists
	cmd = ['glances --export-csv /tmp/glances.csv -t 0.5;hostname > /tmp/hostname.txt']  # commands lists
	# per hosts
	for i in range(71,77):
		ip = '192.168.100.'+str(i)
		a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
		a.start()

