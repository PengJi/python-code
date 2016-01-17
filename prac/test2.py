def f1():
    print 1
f1()

def f2(a):
    print a
f2(1)
f2("sdafa")

def f3(a = 1,b=2,c=3):
    print 'a=',a
    print 'b=',b
    print 'c=',c
    #return a
    return a,b+c
    
f3(1,3,2)
f3(1)
f3(a=1,b=3,c=4)
print f3(a=2,c=3)


c,d = f3(b=4,c=9)
print c
print d


d = f3(b=4,c=9)
print d

fx = f3()
fx

f1 = lambda x,y:x+y
print f1(2,3)
