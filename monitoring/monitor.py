#!/usr/bin/env python

import sys
import time

# monitoring CPU
def cpuinfo():
    lines = open('/proc/stat').readlines()
    for line in lines:
        ln = line.split()
        if ln[0].startswith('cpu'):
            return ln;
    return []

# monitoring mem


# monitoring disk

def disk_stat():
    import os
    hd={}
    disk = os.statvfs("/")
    hd['available'] = disk.f_bsize * disk.f_bavail/(1024*1024*1024)
    hd['capacity'] = disk.f_bsize * disk.f_blocks/(1024*1024*1024)
    hd['used'] = disk.f_bsize * disk.f_bfree/(1024*1024*1024)
    return hd

print disk_stat()

# monitoring net


if __name__ == '__main__':
	print "CPU_per"

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


