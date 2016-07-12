import os
import sys
import urllib
from urlparse import urlparse

#reload(sys)
#sys.setdefaultencoding('utf8')
#print sys.getdefaultencoding()

path = "/home/hadoop/python_prac/file/datatest"
lstdir = os.listdir(path)
#print lstdir
#['2012-06-09', '2012-05-10']

# handle all files in a dirctory
for i,dire in enumerate(lstdir):
	lstfile = os.listdir(path + '/' + dire)
	#print lstfile
	#['A2FBCCA3F9DBF3312E99152C71703E30_2012-06-09_19-54-34.txt', '9A451D5DA4A1E6F25A5074CA0C451979_2012-06-09_06-30-26.txt']
	#['A809AEDEC0625CF63861593F844E3F49_2012-05-10_07-44-23.txt', 'A86C89F9A5C7C0970092D9179FADDC5F_2012-05-10_09-26-23.txt']
	
	# one file/per day
	fileWriteObj = open(str(lstdir[i]), 'a')

	# handle one file
	for files in lstfile:
		#print files
		# A2FBCCA3F9DBF3312E99152C71703E30_2012-06-09_19-54-34.txt
		userlst = files.split('_');
		
		filename = path + '/' + lstdir[i] + '/' +files
		fileReadObj = open(filename)
		fileLineText = fileReadObj.readline()

		# first line
		lastTimeLst = fileLineText.split('<=>')
		lastTime = lastTimeLst[1]

		#jump second line
		fileLineText = fileReadObj.readline()
		fileLineText = fileReadObj.readline()

		# the other lines
		while ('' != fileLineText):
			string = fileLineText
			#print string
			# four conditions:
			# 1. T<=>1258[=]P<=>explorer.exe[=]I<=>136[=]W<=>100a2[=]V<=>6.00.2900.5512
			# 2. T<=>179[=]P<=>chrome.exe[=]I<=>5756[=]U<=>NULL[=]A<=>10304[=]B<=>1030a[=]V<=>17.0.963.79
			# 3. T<=>212[=]P<=>chrome.exe[=]I<=>5756[=]U<=>www.discuz.net[=]A<=>10304[=]B<=>302c8[=]V<=>17.0.963.79
			# 4. T<=>16723[=]P<=>iexplore.exe[=]I<=>5312[=]U<=>http://www.caiwandou.com/admin.php[=]A<=>103b4[=]B<=>70cf0[=]V<=>8.00.7600.16385
			
			# split URL
			urlst = string.split('U<=>')
			url = "none"
			# (2,3,4)URL exists
			if len(urlst) == 2:
				urlstr = urlst[1].split('[=]')[0]
				urltup = urlparse(urlstr)
				# (4)URL include http
				if urltup[1] != '':
					url = urltup[1]
				# (2,3)URL ex http
				else:
					for suf in ['.com','.cn','.net']:
						inde = urltup[2].find(suf)
						# (3)URL ex http and that is a true URL 
						if inde != -1:
							url = urltup[2][0:inde+4]
						# (2)that is not a true URL
						else:
							url = "tst"

			ls = string.split('[=]')
			inputStr = userlst[0] + "\t" + ls[0] + "\t"  + ls[1] + "\t"  + url  + "\n"
			fileWriteObj.write(inputStr)
			fileLineText = fileReadObj.readline()    

		fileReadObj.close()

	fileWriteObj.close()


print "Done" 
