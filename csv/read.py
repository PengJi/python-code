import csv
with open('test', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[3].replace('`','').decode("gb2312")

f.close()
