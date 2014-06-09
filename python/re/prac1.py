#写出同时匹配邮箱和电话号码的正则表达式

#diannao0812@163.com
#15022599293
import re

print 'Please input mail address or phone number:',
inputmail=raw_input()

#p=re.compile('[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$|^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}$')
#p=re.compile('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z]+)*$|\d{3}-\d{8}|\d{4}-\d{7}|(?<!\w)1[2-9]\d{9}(?!\w)')
p = re.compile('[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$\d{3}-\d{8}|\d{4}-\d{7}|(?<!\w)1[2-9]\d{9}(?!\w)')

match = p.match(inputmail)

while True:
    if match:
        print match.group()
        print 'Please input mail address or phone number:',
        inputmail=raw_input()
        match = p.match(inputmail)        
    else:
        print 'mail address or phone number is error!'
        print 'Please input mail address or phone number:'
        inputmail=raw_input()
        match = p.match(inputmail)
    