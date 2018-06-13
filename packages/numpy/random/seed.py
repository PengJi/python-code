#coding: utf-8

import numpy as np

'''
生成器
RandomState([seed]) 
Container for the Mersenne Twister pseudo-random number generator.

seed([seed])    
Seed the generator.

get_state() 
Return a tuple representing the internal state of the generator.

set_state(state)    
Set the internal state of the generator from a tuple.


当设置相同的seed时，每次生成的随机数也相同，
如果不设置seed，则每次生成的随机数也不同
'''

def test_seed():
  a = np.random.rand(5)
  print '第一次a: ', a

  a = np.random.rand(5)
  print '第二次a: ', a

  np.random.seed(3)
  b = np.random.rand(5)
  print '第一次b: ', b

  np.random.seed(3)
  b = np.random.rand(5)
  print '第二次b: ', b


if __name__ == "__main__":
  test_seed()




