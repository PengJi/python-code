#coding: utf-8

import numpy as np

'''
简单随机数
rand(d0, d1, …, dn) 
Random values in a given shape.
产生均匀分布的随机数

randn(d0, d1, …, dn)    
Return a sample (or samples) from the “standard normal” distribution.
产生标注正态分布随机数

randint(low[, high, size, dtype])   
Return random integers from low (inclusive) to high (exclusive).
产生随机数

random_integers(low[, high, size])  
Random integers of type np.int between low and high, inclusive.

random_sample([size])   
Return random floats in the half-open interval [0.0, 1.0).
在[0.0, 1.0)内产生随机数

random([size])  
Return random floats in the half-open interval [0.0, 1.0).
同random_sample

ranf([size])    
Return random floats in the half-open interval [0.0, 1.0).
同同random_sample

sample([size])  
Return random floats in the half-open interval [0.0, 1.0).
同同同random_sample

choice(a[, size, replace, p])   
Generates a random sample from a given 1-D array
从a中随机选择指定数据

bytes(length)   
Return random bytes.
返回随机位
'''

def test_rand():
  print 'rand'

if __name__ == '__main__':
  test_rand()
