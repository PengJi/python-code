#!/usr/bin/env python

# http://xiaoluoge.blog.51cto.com/9141967/1626432

import re,pickle
import psutil
import time
def GetcpuLoad():
    cpuLoad=psutil.cpu_percent(interval=1) 
    return cpuLoad
def GetMeminfo():
    mem = psutil.virtual_memory()
    mem_total = mem.total/1024/1024
    mem_user = mem.used/1024/1024
    mem_free = mem.free/1024/1024
    mem_dic =  {'mem_total':float(mem_total),'mem_user':float(mem_user),'mem_free':float(mem_free)}
    return mem_dic
def GetNetworkinfo(eth):
    networkinfo = psutil.net_io_counters(pernic=True)[eth]
    bytes_sent=list(networkinfo)[0]/1024/1024
    bytes_recv=list(networkinfo)[1]/1024/1024
    total = (bytes_sent+bytes_recv)
    return total
def GetNetworkio():
    networkio = psutil.net_io_counters()
    bytes_sent = list(networkio)[0]/1024/1024
    bytes_recv = list(networkio)[1]/1024/1024
    total = (bytes_sent+bytes_recv)
    return total
def GetdiskIO():
    disk_io = psutil.disk_io_counters()
    read_count =list(disk_io)[0]/1024/1024
    write_count =list(disk_io)[1]/1024/1024
    io_total = (read_count+write_count)
    return io_total
def GetdiskSize():
    disk_list = []
    d_list = []
    total_disk = []
    disk_name=list(psutil.disk_partitions())
    for name in disk_name:
          disk_list.append(list(name)[1])  
          with open('fdisk_list.txt','w') as fd:
              pickle.dump(disk_list,fd)
    with open('fdisk_list.txt','r') as fd:
          fdisk_name = pickle.load(fd)
          for n in fdisk_name:
                fdisk_name_list = n
                total=list(psutil.disk_usage(n))[0]/1024/1024
                used =list(psutil.disk_usage(n))[1]/1024/1024
                free =list(psutil.disk_usage(n))[2]/1024/1024
                d_list=[fdisk_name_list,total,used,free]
                total_disk.append(d_list)
                with open('total_list.txt','w') as fd:
                        pickle.dump(total_disk,fd)
if __name__ =='__main__':
	#print GetMeminfo()
	#print GetNetworkinfo('eth0')
	print GetdiskIO()
