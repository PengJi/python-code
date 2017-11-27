#coding: utf-8

import json as js
import xlwt

# http://blog.csdn.net/qq_23926575/article/details/76566209
# http://blog.csdn.net/destinymf/article/details/78096678

# 创建excel
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

row = 1
col = 1

#设置行表头
worksheet.write(0, 0+col, label='seg0')
worksheet.write(0, 1+col, label='seg1')
worksheet.write(0, 2+col, label='seg2')
worksheet.write(0, 3+col, label='seg3')
worksheet.write(0, 4+col, label='seg4')
worksheet.write(0, 5+col, label='seg5')
worksheet.write(0, 6+col, label='seg6')
worksheet.write(0, 7+col, label='seg7')
worksheet.write(0, 8+col, label='seg8')
worksheet.write(0, 9+col, label='seg9')
worksheet.write(0, 10+col, label='seg10')
worksheet.write(0, 11+col, label='seg11')
worksheet.write(0, 12+col, label='seg12')
worksheet.write(0, 13+col, label='seg13')
worksheet.write(0, 14+col, label='seg14')
worksheet.write(0, 15+col, label='seg15')

#设置列表头
worksheet.write(1, 0, label='default_group')
worksheet.write(2, 0, label='admin_group')
worksheet.write(3, 0, label='rg2')
worksheet.write(4, 0, label='rg3')
worksheet.write(5, 0, label='rg1')

fj = open("test3.json")

data = list()

for line in fj:
  data.append(js.loads(line))

#print data

for list_item in data:
  for key, value in list_item.items():
    if key == "0":
      worksheet.write(row, 0+col, value)
    if key == "1":
      worksheet.write(row, 1+col, value)
    if key == "0":
      worksheet.write(row, 2+col, value)
    if key == "3":
      worksheet.write(row, 3+col, value)
    if key == "4":
      worksheet.write(row, 4+col, value)
    if key == "5":
      worksheet.write(row, 5+col, value)
    if key == "6":
      worksheet.write(row, 6+col, value)
    if key == "7":
      worksheet.write(row, 7+col, value)
    if key == "8":
      worksheet.write(row, 8+col, value)
    if key == "9":
      worksheet.write(row, 9+col, value)
    if key == "10":
      worksheet.write(row, 10+col, value)
    if key == "11":
      worksheet.write(row, 11+col, value)
    if key == "12":
      worksheet.write(row, 12+col, value)
    if key == "13":
      worksheet.write(row, 13+col, value)
    if key == "14":
      worksheet.write(row, 14+col, value)
    if key == "15":
      worksheet.write(row, 15+col, value)

  row +=1

workbook.save('cpu.xls')
fj.close()

