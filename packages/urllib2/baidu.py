# -*- coding: utf-8 -*-

import urllib  #负责url编码处理
import urllib2

url = "http://www.baidu.com/s"
value = raw_input("输入要查询的关键字：")
word = {"wd":value}

#转换成url编码格式（字符串）
word = urllib.urlencode(word) 

  # url首个分隔符就是 ?
newurl = url + "?" + word  

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib2.Request(newurl, headers=headers)
response = urllib2.urlopen(request)
print response.read()