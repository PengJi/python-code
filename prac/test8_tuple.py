#coding=utf-8

#元组
#不可改变，查找效率高
a= (1,2,34,5)
print a

for o in a:
    print o
    
b = [x for x in a] #转化成列表
print b
b = (x for x in a) #生成生成器
print b.next()

print a[1]
print a[:-1]

print 'abc %d and %s\n' %(1,'ssss') #字符串格式化

a = (1,[2,3,4],5)
print a
a[1].append(6) #改变元组中的列表
print a

