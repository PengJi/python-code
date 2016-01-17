#coding=utf-8

#字典
a = {"b":1,"c":2}
print a

if a.has_key('b'):
    print a['b']

#字典的遍历
for o in a.iteritems():
    print o

#输出k值
b = [x for x in a.iterkeys()]
print b

#key值
c = [x for x in a.itervalues()]
print c

print a .values()

e  = sorted(a,key=lambda t:t[0]) #排序
print e

