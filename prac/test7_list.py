#coding=utf-8

#列表
a = [1,2,3,4,5,6,7,8,9,10]
print a
b = [11,12,13]
a.append(b)
print a
a.extend(b)
print a
print a.count(3)
a.insert(1,'a')
print a

#添加路径
#sys.path.insert(1,'usr/bin')

s= a.pop() #抛出队尾元素
print s

a.remove(3) #删除3，只能去除第一个
print a

a = [1,2,3]
a.reverse() #翻转
print a

a = [2,3,5,1,6,9,2,4]
a.sort() #排序
print a

print a[1] 

#切片操作
b= a[:3] #取子集
print b
b = a[2:5] #取子集
print b

print a[-1]





