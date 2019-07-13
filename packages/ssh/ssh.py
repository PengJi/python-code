# -*- coding: utf-8 -*-

import ssh

# http://blog.sina.com.cn/s/blog_53d874320102vdvu.html

myclient = ssh.SSHClient()
ient.set_missing_host_key_policy(ssh.AutoAddPolicy())
myclient.connect("192.168.100.72", port=22, username="scidb", password="scidb")
stdin, stdout, stderr = client.exec_command("ls -l")
print stdout.read()
