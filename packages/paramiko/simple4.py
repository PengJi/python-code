#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现堡垒机模式下的远程文件上传
原理是通过paramiko的SFTPClient将文件从办公设备上传至堡垒机的临时目录，如/tmp，
再通过SSHClient的invoke_shell方法开启 ssh 会话，执行 scp 命令，
将/tmp 下的指定文件复制到目标业务服务器上。

下面示例使用 sftp.put() 方法上传文件至堡垒机临时目录，再通过 send() 方法执行与 scp 命令，
将堡垒机临时目录下的文件复制到目标主机。
"""

import paramiko
import sys

hostname = "192.168.1.21"  # 定义堡垒机信息
username = "root"
password = "SKJh935yft#"

blip = "192.168.1.23"  # 定义业务服务器信息
bluser = "root"
blpasswd = "SKJh935yft#"

tmpdir = "/tmp"
remotedir = "/data"
localpath = "/home/nginx_access.tar.gz"  # 本地源文件路径
tmppath = tmpdir+"/nginx_access.tar.gz"  # 堡垒机临时路径
remotepath = remotedir + "/nginx_access_hd.tar.gz"  # 业务主机目标路径

port = 22
passinfo = '\'s password: '
paramiko.util.log_to_file('syslogin.log')

t = paramiko.Transport((blip, port))
t.connect(username=bluser, password=blpasswd)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath, tmppath)  # 上传本地源文件到堡垒机临时路径
sftp.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

# new session
channel = ssh.invoke_shell()
channel.settimeout(10)

buff = ''
resp = ''
# scp 中转目录文件到目标主机
channel.send('scp '+tmppath+' '+username+'@'+hostname+':'+remotepath+'\n')

while not buff.endswith(passinfo):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print('Error info:%s connection time.' % (str(e)))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''

channel.send(password+'\n')

buff = ''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print('Error info: Authentication failed.')
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp

print(buff)
channel.close()
ssh.close()
