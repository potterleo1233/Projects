import csv

isplist = open("isps1.txt").readlines()
tloglist = open("tlogs1.txt").readlines()


for line in tloglist:
	tlogname = line.split("\t")[0]
	tlogdate = line.split("\t")[1]
	if tlogname == "":
		tlogname = "other_events"
	with open(tlogname +".txt","a") as file:
		file.write(line)
		with open("isps1.txt") as ispfile:
			for search in ispfile:
				ispname = search.split("\t")[0]
				ispdate = search.split("\t")[1]
				if ispname == tlogname and ispdate == tlogdate:
					file.write(search)







#List = open("temporary.txt").readlines()
#with open("temporary1.csv","a") as csvfile:
#    ListWriter = csv.writer(csvfile, delimiter=',', quotechar="-")
#    for x in List:
#        x = x.replace(",","")
#        x = x.replace("\t",",")
#        x = x.replace("\n","")
#        y = x.split(",")
#        csp = y[3].split('/')
#        x = (csp[0] + "," + y[4] + "," + y[1] + "," + y[2] + "\n")
#        print (x)
#        csvfile.write(x)
#        ListWriter.writerow([y[3],y[4],y[1],y[2]])
##file = open("temporary1.csv").readlines()
##for line in file:
##    if line.strip():
##        print (line)