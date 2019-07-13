globalVar = 100           #G

def test_scope():
    enclosingVar = 200    #E
    def func():
        localVar = 300    #L
print __name__            #B
