import csv

lst=[]
tup=('testtup')

with open('demographic.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print row[0] + row[1].decode('UTF8') + row[2] + row[3].decode('UTF8') + row[4].decode('UTF8') + row[5].decode('UTF8') + row[6].decode('UTF8') + row[7].decode('UTF8') + row[8].decode('UTF8')
		#tup = (row[0],row[1].decode('UTF8'),row[2],row[3].decode('UTF8'),row[4].decode('UTF8'),row[5].decode('UTF8'),row[6].decode('UTF8'),row[7].decode('UTF8'),row[8].decode('UTF8'))
		tup = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
		lst.append(tup)

f.close()

with open('demographic1.csv','wb') as f:
	writer = csv.writer(f)
	writer.writerows(lst)

f.close()

print lst
