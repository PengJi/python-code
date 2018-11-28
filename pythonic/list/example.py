# -*- coding: utf-8 -*-

""" 列表排序 """
lst = [1, 2, 9, 10, -2, -4, -5, -12]
""" 排序，把正的放在前面，负的放在后面，并且分别按绝对值从大到小排序 """
lst.sort(key=lambda x: (x < 0, abs(x)))
print lst

""" 列表推导 """
print [i*i for i in range(30,41) if i%2==0]

""" 集合推导 """
print {i*i for i in range(1,20) if i %2 != 0}

""" 字段推导 """
print {i:i*i for i in range(30,40) if i%2 !=0}
