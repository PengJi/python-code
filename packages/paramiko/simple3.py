#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现堡垒机模式下的远程命令执行
可以利用paramiko的invoke_shell机制来实现通过堡垒机实现服务器操作，
原理是SSHClient.connect到堡垒机后开启一个新的SSH会话(session)，
通过新的会话运行"ssh user@IP"去实现执行命令的操作。
"""

import paramiko
import sys

hostname = "192.168.1.21"  # 定义堡垒机信息
username = "root"
password = "SKJh935yft#"

blip = "192.168.1.23"  # 定义业务服务器信息
bluser = "root"
blpasswd = "SKJh935yft#"

port = 22
passinfo = '\'s password: '  # 输入服务器密码的前标志串
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()  # ssh登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, username=bluser, password=blpasswd)

# new session
channel = ssh.invoke_shell()  # 创建会话，开启命令调用
channel.settimeout(10)  # 会话命令执行超时时间，单位为秒

buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n')  # 执行 ssh 登录业务主机

while not buff.endswith(passinfo):  # ssh登录的提示信息判断，输出串尾含有"\'s password:"时，退出while循环
    try:
        resp = channel.recv(9999)
    except Exception, e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    if not buff.find('yes/no') == -1:  # 输出串尾含有"yes/no"时发送"yes"并回车
        channel.send('yes\n')
        buff = ''

channel.send(password+'\n')  # 发送业务主机密码

buff = ''
while not buff.endswith('# '):  # 输出串尾为"# "是说明校验通过并退出while循环
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:  # 输出串尾含有"\'s password: "时说明密码不正确，要求重新输入
        print 'Error info: Authentication failed.'
        channel.close()  # 关闭连接对象后退出
        ssh.close()
        sys.exit()
    buff += resp

channel.send('ifconfig\n')  # 认证通过后发送ifconfig命令来查看结果
buff = ''
try:
    while buff.find('# ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception, e:
    print "error info:"+str(e)

print buff  # 打印输出串
channel.close()
ssh.close()
