import os

path = "./tmp"
lstdir = os.listdir(path)

for i,dire in enumerate(lstdir):
	print dire
	#2012-06-09
	#2012-05-10

	fileWriteObj = open('./result' + '/' + str(lstdir[i]), 'a')
	for line in reversed(open(dire).readlines()):
		strlst = line.split("\t")
		print strlst
