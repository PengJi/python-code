#coding=utf-8

# 类的定义
class a:
    def __init__(self):  # 构造函数
        self.m = 1  # a类的成员变量

    def add(self):  # 定义成员函数
        self.p=4
        print(self.m+self.p)
        
# 类的继承
class b(a):
    def __init__(self):
        a.__init__(self)
        self.n = 2
        self.tt()

    def sum(self, a=1, b=2):
        """帮助文档信息"""   # 文档字符串的使用
        print(self.m+self.n)
        self.__dd()

    def tt(self):
        self.m = 6

    def __dd(self):  # 私有函数
        print("dd")

    def __ee__(self):  # 专有函数
        print("ee")
        if 1 == 2:
            pass
        try:
            fun()
        except Exceptiona as e:
            print(e.message)

    def funx(self):
        pass


c = b()
c.sum()
c.add()
c.__ee__()


class Animal():
    def __init__(self, name):
        self.name = name

    def saySomething(self):
        print("I am " + self.name)


class Dog(Animal):
    def __init__(self, name):
        super(Animal, self).__init__(name)

    def saySomething(self):
        print ("I am " + self.name + ", and I can bark")

    def animal_say_1(self):
        # 子类调用父类的方法
        #  方式1
        super(Dog, self).saySomething()

    def animal_say_2(self):
        #  方式2 [推荐]
        super(Animal, self).saySomething()

    def animal_say_3(self):
        # 方式3
        Animal.saySomething(self)


if __name__ == "__main__":
    dog = Dog("Blake")
    dog.saySomething()
    dog.animal_say_1()
    dog.animal_say_2()
    dog.animal_say_3()
    # 子类对象调用被覆盖的父类方法
    super(Dog, dog).saySomething()