#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现密钥方式登录远程主机
实现自动密钥登录方式，第一步需要配置与目标设备的密钥认证支持，密钥文件可以存放在默认路径 ~/.ssh/id_rsa，
也可以自定义，通过paramiko.RSAKey.from_private_key_file()方法引用
"""

import paramiko
import os


hostname = '192.168.1.21'
username = 'root'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('/home/key/id_rsa')  # 定义私钥存放路径
key = paramiko.RSAKey.from_private_key_file(privatekey)  # 创建私钥对象 key

ssh.connect(hostname=hostname, username=username, pkey=key)
stdin, stdout, stderr = ssh.exec_command('free -m')
print(stdout.read())
ssh.close()
