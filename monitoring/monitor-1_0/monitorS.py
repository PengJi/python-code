#!/usr/bin/env python

import os
import sys
import time
import psutil
import threading
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
	'''
	if os.path.isfile('/tmp/monitor_cpu.txt'):
		os.remove('/tmp/monitor_cpu.txt')
	'''
	cpuWriteObj = open('/tmp/monitor_cpu.txt',"a")
	cpuWriteObj.write("CPU percent\n")
	while True:
		time.sleep(0.5)
		W = cpuinfo()
		cpuTotal = long(W[1])+long(W[2])+long(W[3])+long(W[4])+long(W[5])+long(W[6])+long(W[7])+long(W[8])+long(W[9])
		cpuIdle = long(W[4])
		cpuused=float(cpuTotal-cpuIdle)/cpuTotal
		print Fore.BLUE + '%.2f%%'%(cpuused*100)
		str_cpu = '%.2f%%'%(cpuused*100) + "\n"
		cpuWriteObj.write(str_cpu)
		cpuWriteObj.flush()
	cpuWriteObj.close()
	

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
	'''
	if os.path.isfile('/tmp/monitor_mem.txt'):
		os.remove('/tmp/monitor_mem.txt')
	'''
	memWriteObj = open('/tmp/monitor_mem.txt',"a")
	title_mem = 'Memory_Total      Memory_Used        Used_Per' + "\n"
	memWriteObj.write(title_mem)
	STATS = Memory()
	try:
		print 'Memory_Total      Memory_Used        Used_Per' + "\n"
		while True:
			time.sleep(0.5)
			Memory()
			MemT = STATS[0]
			MemU = STATS[1]
			Used_Per = STATS[2]
			print Fore.CYAN,MemT ,'KB,',MemU ,'KB,',Used_Per
			str_mem = str(MemT) + ',' + str(MemU)  + ','+ str(Used_Per) + "\n"
			memWriteObj.write(str_mem)
			memWriteObj.flush()

	except KeyboardInterrupt, e:
		print "\nmemmonit exited"
	finally:
		memWriteObj.close()


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
	'''
	if os.path.isfile('/tmp/monitor_IO.txt'):
		os.remove('/tmp/monitor_IO.txt')
	'''
	ioWriteObj = open('/tmp/monitor_IO.txt',"a")
	title_IO = "read_bytes,write_bytes,read_time,write_time" + "\n"
	ioWriteObj.write(title_IO)
	print "read_bytes,write_bytes,read_time,write_time"
	while True:
		time.sleep(0.5)
		disk_cur = disk_IO()
		disk_con['read_bytes'] = disk_cur['read_bytes'] - disk_start['read_bytes']
		disk_con['write_bytes'] = disk_cur['write_bytes'] - disk_start['write_bytes']
		disk_con['read_time'] = disk_cur['read_time'] - disk_start['read_time']
		disk_con['write_time'] = disk_cur['write_time'] - disk_start['write_time']
		print Fore.YELLOW,disk_con['read_bytes'],",",disk_con['write_bytes'],',',disk_con['read_time'],',',disk_con['write_time']
		str_io =  str(disk_con['read_bytes']) + ',' + str(disk_con['write_bytes']) + ',' +str(disk_con['read_time']) + ',' + str(disk_con['write_time']) + "\n"
		ioWriteObj.write(str_io)
		ioWriteObj.flush()
	ioWriteObj.close()
	

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
	'''
	if os.path.isfile('/tmp/monitor_net.txt'):
		os.remove('/tmp/monitor_net.txt')
	'''
	netWriteObj = open('/tmp/monitor_net.txt',"a")
	title_net = 'In   Out' + "\n"
	netWriteObj.write(title_net)
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
		print Fore.MAGENTA,RX_RATE ,'KB  ',TX_RATE ,'KB'
		str_net = str(RX_RATE) + ',' + str(TX_RATE) + ',' + "\n"
		netWriteObj.write(str_net)
		netWriteObj.flush()
	netWriteObj.close()


if __name__ == '__main__':
	#monitor_cpu()
	#monitor_mem()
	#monitor_IO()
	#monitor_net()

	thread_cpu = threading.Thread(target=monitor_cpu, args=())
	thread_cpu.start()
	thread_mem = threading.Thread(target=monitor_mem, args=())
	thread_mem.start()
	thread_IO = threading.Thread(target=monitor_IO, args=())
	thread_IO.start()
	thread_net = threading.Thread(target=monitor_net, args=())
	thread_net.start()

	print Style.RESET_ALL
