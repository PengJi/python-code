from pyDOE import *
from numpy import *

# MPL2
def get_mpl2():
    origin_mpl_2 = lhs(2,10)
    print origin_mpl_2
    print ceil(origin_mpl_2*10)

# MPL3
def get_mpl3():
    origin_mpl_3 = lhs(3,10)
    print origin_mpl_3

# MPL4
def get_mpl4():
    origin_mpl_4 = lhs(4,10)
    print origin_mpl_4

# MPL5
def get_mpl5():
    origin_mpl_2 = lhs(5,10)
    print origin_mpl_5
    
if __name__ == '__main__':
    get_mpl2()
