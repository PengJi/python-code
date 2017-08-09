# coding: utf-8
import  xdrlib,sys
import xlrd
import xlwt

def open_excel(file='test.xlsx'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception,e:
		print str(e)

# 根据索引获取Excel表格中的数据   
# 参数:
# file：Excel文件路径     
# colnameindex：表头列名所在行的所以 
# by_index：表的索引
def excel_table_byindex(file= 'test.xlsx',colnameindex=0,by_index=0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #行数
	ncols = table.ncols #列数
	colnames =  table.row_values(colnameindex) #某一行数据 
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}	
			for i in range(len(colnames)):
				app[colnames[i]] = row[i] 
			list.append(app)
	return list

# 根据名称获取Excel表格中的数据   
# 参数:
# file：Excel文件路径     
# colnameindex：表头列名所在行的所以  
# by_name：Sheet1名称
def excel_table_byname(file= 'test.xlsx',colnameindex=0,by_name=u'data_load'):
	data = open_excel(file)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows #行数 
	colnames =  table.row_values(colnameindex) #某一行数据 	
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[colnames[i]] = row[i]
			list.append(app)
	return list

# 得到某一个单元格的值
def get_cell(file='test.xlsx',index_sheet=6,index_row=0,index_col=0):
	data = open_excel(file)
	table = data.sheets()[index_sheet]
	return table.cell(index_row,index_col).value
	#return table.row(index_row)[index_col].value
	#return table.col(index_col)[index_row].value

# 设置某一个单元格的值
# 参数:
# file: 
# index_sheet:
# index_row:
# index_col:
# ctype: 数据类型,0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
# xf: 扩展的格式化, 默认是0
def set_cell(file='test.xlsx',index_row=0,index_col=0,ctype=2,):
	data = xlwt.Workbook()
	table = data.add_sheet()


def main():
	tables = excel_table_byindex()
	for row in tables:
		print str(row).decode("unicode_escape").encode("utf8")

	tables = excel_table_byname()
	for row in tables:
		print str(row).decode("unicode_escape").encode("utf8")

	val = get_cell('test.xlsx',0,3,1)
	print val

if __name__=="__main__":
	main()
