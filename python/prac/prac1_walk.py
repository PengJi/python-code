#coding=utf-8
# os.walk()的使用  

import os  
# 枚举dirPath目录下的所有文件  

#取得操作系统分隔符，以支持在不同平台上运行
#sep=os.path.sep
def main():  
#begin  
    fileDir = r"D:\Python27" 
    for root, dirs, files in os.walk(fileDir):  
        #输出子文件夹
        print  u"文件夹："
        for dir in dirs:  
            print(os.path.join(root, dir))  
        #输出文件名
        print u"文件："
        for file in files:  
            print file
            #print(os.path.join(root, file))  
            

main()