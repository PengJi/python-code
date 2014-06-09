f = open(r"C:\Users\admin\Desktop\python task.txt")
#从第5个字节开始读取
#f.seek(5)
#读取每一行
#while True:
    #line = f.readline()
    #print line
    #if line == '':
        #break
    
print f.read()
f.close()