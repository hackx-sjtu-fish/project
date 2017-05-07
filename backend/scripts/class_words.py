import json

infile = file("emoji_splitted.csv","rb")
outfile = file("keywords.json","wb")

line=infile.readline()
l=[]

while line!="":
    for i in line.replace("\n","").split(",")[1:]:
        l.append(i)
    line=infile.readline()

s=set(l)
l=list(s)
outfile.write(json.dumps(l))
outfile.close()
