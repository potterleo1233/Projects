import sys,os,subprocess,csv
Aline = []
dates = []
staff = []
blue = []
EndOfTheLine = [['program','Date','Staff','Result','Comment']]
thisfile = sys.argv[1]
thatfile = sys.argv[2]
outfile = open(thatfile,'w')
csvwriter = csv.writer(outfile, delimiter=',',lineterminator='\n',quotechar='"', quoting=csv.QUOTE_MINIMAL)
#output = csv.DictWriter(open('file3.csv','w'), delimiter=',', lineterminator='\n', fieldnames=headers)
with open(thisfile) as f:
    data = f.readlines()
    lines_set = set(data)
    for things in lines_set:
        blue.append(things)
    for line in (blue):
        line = line.rstrip()
#        line = line.replace("\t",",")
        line = line.replace(" \n","")
        line = line.split("\t")
        for a in [line]:
            Aline.append(a)
for line in Aline:
    if len(line) > 2:
        if line[2] == ("Begin Time:"):
            dates = line[1]
            line = [""]
        if line[0] == ('Location:'):
            staff = line[3]
            line = [""]
        if line[0] == ("Task"):
            line = [""]
    line = list(filter(None, line))
    if len(line) > 1:
        line.append(staff)
        line.append(dates)
        #line = (line[0],line[-1],line[1:-1])
        if len(line) == 4:
            line = [line[0],line[-1],line[2],line[1]]
        if len(line) == 5:
            line = [line[0],line[-1],line[3],line[1],line[2]]
        EndOfTheLine.append(line)

'''for line in EndOfTheLine:
    csvwriter.writerow(line)
'''