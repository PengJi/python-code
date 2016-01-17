#coding=utf-8

import os

#map
a = [1,2,3,4,5]
b = map(lambda x:x*2,a) #分别乘2
print b

#reduce
c = reduce(lambda x,y:x+y,a) #归并
print c

#filter
d = filter(lambda x:x%2,a) #返回奇数
print d

d= filter(lambda x:not x%2,a) #返回偶数
print d


b = os.walk('.') #b为生成器
print [o for o in b]

b = os.walk('.')
b.next()

def fab(m):
    a,b = 1,1
    while a<m:
        yield a #声明生成器
        a,b = b,a+b
        
b = fab(6) #生成器
print b.next()
print b.next()
print b.next()
print b.next()