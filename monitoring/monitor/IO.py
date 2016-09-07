#!/usr/bin/env python
#coding=utf8

# http://www.0550go.com/script/python/python-psutil-disk-io.html
 
import psutil
import sys
 
class DiskIo(object):
    def __init___(self):
        self.read_count = 0
        self.write_count = 0
    def get_io_read_count(self):
        a = psutil.disk_io_counters(perdisk=True)
        self.read_count = a['sda4'][0]
        return self.read_count
    def get_io_write_count(self):
        a = psutil.disk_io_counters(perdisk=True)
        self.write_count = a['sda4'][1]
        return self.write_count
 
class error_out(object):
    def error_out(self):
        '''输出错误信息'''
        print
        print 'Usage : ' + sys.argv[0] + ' StatusKey '
        print
        sys.exit(1)
 
class Main(object):
    def main(self):
        if len(sys.argv) == 1:
            error = error_out()
            error.error_out()
        elif sys.argv[1] == 'read_count':
            a = DiskIo()
            print a.get_io_read_count()
        elif sys.argv[1] == 'write_count':
            a = DiskIo()
            print a.get_io_write_count()
if __name__ == '__main__':
    main_obj = Main()
    main_obj.main()
