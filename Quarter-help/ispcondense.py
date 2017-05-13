import operator,sys,os,subprocess,csv
#here we declare needed variables for later on
SpecialProgram = []
NormalForm = []
SorList = []
Layer0 = []
Layer1 = []
series = []
Staff = []
#infile = 'hpisp.txt' #kept for testing and debugging
#outfile = open('hpisp.csv','w') #kept for testing and debugging
#these two variables are important as they will be our in and out files. Used later in the program
infile = sys.argv[1]
if infile[-3:] == 'txt':
    outfile = open(infile[:-3] + "csv",'w')
#this is for later writing the csv file, it has to be declared here.
csvwriter = csv.writer(outfile, delimiter=',',lineterminator='\n',quotechar='"', quoting=csv.QUOTE_MINIMAL)
'''
This bit prepares the file by deleting empty lines and splitting up all the lines by tabs making it easy to manipulate later
'''
for Firsplit in open(infile): # splits each line into one entry on a list
    Firsplit = Firsplit.replace("\n","") # replaces the newline characters at the end of each line to make the end product prettier
    series.append(Firsplit)
series = [v for i, v in enumerate(series) if series[1:i].count(v) == 0]
for Field in series:
    if not Field.rstrip(): continue # if the line is empty skip it
    Layer0.append(Field.split("\t")) # split up each line by tabs
'''This long bit extracts the dates and staff names along with ordering the data and preparing it for the
CSV file later on'''
for Item in Layer0:
    if len(Item) > 1:
        if Item != []:
            if Item[0] == ("Comment: "):
                Item.insert(2," ")
    if len(Item) > 2:
        if len(Item[0]) > 6:
            if Item[0][2] == ("/"): #find (date first) lines
                SpecialProgram.append(("Special Program",Item[0],Item[5],Item[6])) # add entries to the final form doc
                Item = [] # clears the line if  used
        if Item != []:
            if Item[1][0] == ("0") or Item[1][0] == ("1"): #find "date: " lines
                Dates = Item[1] # aquires dates from the "date: " first line
                Item = []
        if Item != [] :
            if Item[2] == ("Service Provider: "): # find staff variable
                Staff = Item[3]
                Item = [] # clear line after use
        if Item != [] :
            if Item[0] == ("Task "): # cut the task line
                Item = []
        if Item != []:
            if Item[0] == ("Comment: "):
                Item.extend((Dates,Staff))
                NormalForm.append((Item[0],Item[3],Item[-1],Item[2],Item[1]))
                Item = []
        if Item != [] :
            if Item[2] != [" "]:
                Item.extend((Dates,Staff))
                NormalForm.append((Item[0],Item[3],Item[-1],Item[1],Item[2]))
                Item = []
    else: continue
for a in NormalForm:
    SorList.append(a)
for s in SpecialProgram:
    SorList.append(s)
LastList = (sorted(SorList, key=lambda list: list[0]))
#This writes to the actual CSV file
Header = "Program","Date","Staff","Isp Result","Comments"
csvwriter.writerow(Header)
for item in LastList:
    csvwriter.writerow(item)

