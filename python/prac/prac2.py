#coding=utf-8

#对一个列表[1,3,5,7,8,9,4] 用map返回乘方列表；reduce计算乘积、filter挑出奇数 ，代码以及过程截图贴到作业中

a = [1,3,5,7,8,9,4]

#map
b = map(lambda x:x*x,a) #分别乘2
print b

#reduce
c = reduce(lambda x,y:x*y,a) #归并
print c

#filter
d = filter(lambda x:x%2,a) #返回奇数
print d
