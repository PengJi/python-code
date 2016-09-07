#!/usr/bin/env python

import os
import sys
import time
import psutil
from colorama import Fore, Back, Style

# monitoring CPU
def cpuinfo():
    lines = open('/proc/stat').readlines()
    for line in lines:
        ln = line.split()
        if ln[0].startswith('cpu'):
            return ln;
    return []

def monitor_cpu():
	print Fore.BLUE + "CPU_per"
	while True:
		time.sleep(0.5)
		W = cpuinfo()
		cpuTotal = long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])+long(W[8])+long(W[9])
		cpuIdle = long(W[4])
		cpuused=float(cpuTotal-cpuIdle)/cpuTotal
		print '%.2f%%'%(cpuused*100)
	

# monitoring mem
def Memory():
	STATS = []
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
	return STATS

def monitor_mem():
	print Fore.CYAN + "mem monitoring"
	STATS = Memory()
	try:
		print 'Memory_Total      Memory_Used        Used_Per' 
		while True:
			time.sleep(0.5)
			Memory()
			MemT = STATS[0]
			MemU = STATS[1]
			Used_Per = STATS[2]
			print MemT ,'KB     ',MemU ,'KB       ',Used_Per  
	except KeyboardInterrupt, e:
		print "\nmemmonit exited"


# monitoring disk
def disk_IO():
	disk_use = {}
	disk_io = psutil.disk_io_counters()
	# in bytes
	disk_use['read_bytes'] = list(disk_io)[2]
	disk_use['write_bytes'] = list(disk_io)[3]
	# in ms
	disk_use['read_time'] = list(disk_io)[4]
	disk_use['write_time'] = list(disk_io)[5]

	return disk_use

def monitor_IO():
	print Fore.YELLOW + "IO monitoring"
	disk_start = disk_IO()
	disk_con = {}
	print "read_bytes,write_bytes,read_time,write_time"
	while True:
		time.sleep(0.5)
		disk_cur = disk_IO()
		disk_con['read_bytes'] = disk_cur['read_bytes'] - disk_start['read_bytes']
		disk_con['write_bytes'] = disk_cur['write_bytes'] - disk_start['write_bytes']
		disk_con['read_time'] = disk_cur['read_time'] - disk_start['read_time']
		disk_con['write_time'] = disk_cur['write_time'] - disk_start['write_time']
		print disk_con['read_bytes'],",",disk_con['write_bytes'],',',disk_con['read_time'],',',disk_con['write_time']
	

# monitoring net
def net_stat():
	ifstat = open('/proc/net/dev').readlines()
	STATS = []
	if len(sys.argv) > 1:
		INTERFACE = sys.argv[1]
	else:
		INTERFACE = 'eth0'

	#print 'Interface:',INTERFACE
	for interface in  ifstat:
		if INTERFACE in interface:
			stat1 = float(interface.split(":")[1].split()[0])
			stat2 = float(interface.split()[9])
			STATS[0:] = [stat1]
			STATS[1:] = [stat2]
	return STATS

def monitor_net():
	print Fore.MAGENTA + "net monitoring"
	STATS_start = net_stat()
	print 'In   Out'
	while True:
		time.sleep(0.5)
		STATS_cur = net_stat()
		rxstat_start = list(STATS_start)
		RX_cur = float(STATS_cur[0])
		RX_start = rxstat_start[0]
		TX_cur = float(STATS_cur[1])
		TX_start = rxstat_start[1]
		RX_RATE = round((RX_cur - RX_start)/1024,3)
		TX_RATE = round((TX_cur - TX_start)/1024,3)
		print RX_RATE ,'KB  ',TX_RATE ,'KB'


if __name__ == '__main__':
	#monitor_cpu()
	#monitor_mem()
	#monitor_IO()
	monitor_net()

	print Style.RESET_ALL
