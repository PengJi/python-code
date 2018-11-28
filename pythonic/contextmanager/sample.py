"""
上下文管理器
控制代码执行前的准备动作以及执行后的收尾工作
"""
""" 打开文件 """
with open(r'data.txt') as myfile:
    for line in myfile:
        pass
""" 管理多个资源 """
with open('data.txt') as source, open('target.txt', 'w') as target:
    target.write(source.read())

""" 上下文管理器管理锁 """
class fetchurl(threading.Thread)
    def run(self):
        with self.lock:
        print 'lock acquired by %s' % self.name
        print 'lock released by %s' % self.name

""" 上下文管理器管理数据库 cursor """
import pymysql

def get_conn(**kwargs):
    return pymysq.connect(host=kwargs.get('host','localhost'),
            port=kwargs.get('port',3306),
            user=kwargs.get('user'),
            passwd=kwargs.get('passwd')

def main():
    conn = get_conn(user='test', passwd='test')
    with conn as cur:
        cur.execute('show database')
        print cur.fetchall()

if __name__ == '__main__':
    main()

