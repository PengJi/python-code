#coding: utf-8

import numpy as np

'''
分布
'''

'''
numpy.random.normal(loc=0.0, scale=1.0, size=None)
loc: float or array_like of floats 
此概率分布的均值
scale: float or array_like of floats 
此概率分布的标准差（对应于宽度，scale越大越矮胖，scale越小，越瘦高
size: int or tuple of ints, optional
'''
def normal():
  mu, sigma = 0, 0.1
  s = np.random.normal(mu, sigma, 10)
  print s

def test():
  mu, sigma = 22.6, 1.5
  s = np.random.normal(mu, sigma, 10)
  print s


if __name__ == "__main__":
  #normal()
  test()
