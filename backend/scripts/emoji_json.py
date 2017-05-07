import json

infile = file("emoji_num.csv","rb")
outfile = file("emoji_unicode.json", "wb")

list = []

line = infile.readline()

while line!="":
    # tmp=[]
    # for i in line.replace("\n","").split(",")[2:]:
    #     tmp.append(int(i))
    list.append(line.replace("\n","").split(",")[0])
    line = infile.readline()

outfile.write(json.dumps(list))
outfile.close()
