#��Ķ���
class a:
    def __init__(self):#���캯��
        self.m = 1#a��ĳ�Ա����
    def add(self):#�����Ա����
        self.p=4
        print self.m+self.p
        
        
#��ļ̳�
class b(a):
    def __init__(self):
        a.__init__(self)
        self.n = 2
        self.tt()
    def sum(self,a=1,b=2):
        """�����ĵ���Ϣ""" #�ĵ��ַ�����ʹ��
        print self.m+self.n
        self.__dd()
    def tt(self):
        self.m = 6
    def  __dd(slef):# ˽�к���
        print "dd"
    def __ee__(self): #ר�к���
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