#类的定义
class a:
    def __init__(self):  #构造函数
        self.m = 1  #a类的成员变量
    def add(self):  #定义成员函数
        self.p=4
        print self.m+self.p
        
#类的继承
class b(a):
    def __init__(self):
        a.__init__(self)
        self.n = 2
        self.tt()
    def sum(self,a=1,b=2):
        """帮助文档信息"""   #文档字符串的使用
        print self.m+self.n
        self.__dd()
    def tt(self):
        self.m = 6
    def  __dd(slef):  #私有函数
        print "dd"
    def __ee__(self):  #专有函数
        print "ee"
        if 1==2:
            pass
        try:
            fun()
        except Exception,e:
            print e.message
    def funx(self):
        pass


c = b()
c.sum()
c.add()
c.__ee__()
