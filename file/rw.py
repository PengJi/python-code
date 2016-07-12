import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()

path = "/home/hadoop/python_prac/file/datatest"
lstdir = os.listdir(path)
#print lstdir
#['2012-06-09', '2012-05-10']
for i,dire in enumerate(lstdir):
	lstfile = os.listdir(path + '/' + dire)
	#print lstfile
	#['A2FBCCA3F9DBF3312E99152C71703E30_2012-06-09_19-54-34.txt', '9A451D5DA4A1E6F25A5074CA0C451979_2012-06-09_06-30-26.txt']
	#['A809AEDEC0625CF63861593F844E3F49_2012-05-10_07-44-23.txt', 'A86C89F9A5C7C0970092D9179FADDC5F_2012-05-10_09-26-23.txt']
	
	# one file/per day
	fileWriteObj = open(str(lstdir[i]), 'a')

	for files in lstfile:
		#print files
		# A2FBCCA3F9DBF3312E99152C71703E30_2012-06-09_19-54-34.txt
		userlst = files.split('_');

		filename = path + '/' + lstdir[i] + '/' +files
		fileReadObj = open(filename)
		fileLineText = fileReadObj.readline()

		while ('' != fileLineText):
			string = fileLineText
			#print string
			# T<=>1258[=]P<=>explorer.exe[=]I<=>136[=]W<=>100a2[=]V<=>6.00.2900.5512
			
			ls = string.split('[=]')
			#print ls
			print ls[0]
			inputStr = userlst[0] + "\t"  + ls[0] + "\n"
			fileWriteObj.write(inputStr)
			fileLineText = fileReadObj.readline()    

		fileReadObj.close()

	fileWriteObj.close()

print "Done" 
