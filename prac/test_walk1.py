#coding=utf-8
# os.walk()的使用  

import os  
# 枚举dirPath目录下的所有文件  

#取得操作系统分隔符，以支持在不同平台上运行
#sep=os.path.sep
def main():  
    fileDir = r"D:\Python27" 
    count = 1
    for root, dirs, files in os.walk(fileDir):  
        if count == 1:
            count = count +1
            print fileDir
            for file in files:  
                print "\t" + file    
            lastRoot = root
            continue
        print root
        #循环输出文件名
        for file in files:  
            str =os.path.join(root, file)
            tabCount = str.count('\\')
            if tabCount == 3:
                print "\t" * (tabCount-1) + file 
            elif tabCount == 4:
                print "\t" * (tabCount-1) + file 
            elif tabCount == 5:
                print "\t" * (tabCount-1) + file 
            else:
                print "\t" * (tabCount-1) + file 
            
main()