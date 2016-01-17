#coding=utf-8

import os

def main():
    print "Hello world"
    
    print "这是Alice\'问候"
    print '这是Bob\'问候'
    
    foo(5,10) #函数调用
    
    print '=' * 10 #字符可乘
    print '这将直接执行' + os.getcwd() #调用了os模块中的函数
    
    counter = 0
    counter += 1
    
    food = ['苹果','杏子','李子','梨']
    for i in food:
        print '俺就爱整只：' + i
        
    print '数到10'
    for i in range(10):
        print i
        
def foo(paraml,secondParam):
    res = paraml+secondParam
    print "%s 加 %s等于 %s" %(paraml,secondParam,res)
    if res<50:
        print "这个"
    elif (res>=50) and ((paraml == 42) or (secondParam == 24)):
        print "那个"
    else:
        print "嗯。。。"
        return res
    '''多行
    注释'''
   
if __name__=='__main__':
    main()