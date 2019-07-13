# -*- coding: utf-8 -*-

# http://www.cnblogs.com/ma6174/archive/2012/05/25/2508378.html

import paramiko
import threading


def ssh2(ip,username,passwd,cmd):

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            #stdin.write("Y")  # simple interaction, enter 'Y'
            out = stdout.readlines()
            # screen print
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except:
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    cmd = ['cal','echo $PATH','hostname']  # commands list
    username = "scidb"  # username
    passwd = "scidb"    # password
    threads = []   # multi-thread
    print "Begin......"
    for i in range(71,77):
        ip = '192.168.100.'+str(i)
        a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        a.start()
