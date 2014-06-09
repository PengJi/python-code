#coding=utf-8

#yield
#http://f.dataguru.cn/forum.php?mod=viewthread&tid=96221
#http://blog.donews.com/limodou/archive/2006/09/04/1028747.aspx

def gen():
    #print 'enter'
    yield 1
    #print 'next'
    yield 2
    print 'next again'

a = gen()
print a.next()

for i in gen():
    print i
    
