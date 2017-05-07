import json

infile1=file("emoji_splitted.csv","rb")
infile2=file("keywords.json","rb")
outfile=file("emoji_num.csv","wb")

class_words=json.loads(infile2.read())

line=infile1.readline()

while line!="":
    line=line.replace("\n","").replace("\r","").split(",")
    outfile.write(line[0])
    tmp=[ class_words.index(word) for word in line[1:] if not word == ""]
    for i in tmp:
        outfile.write(","+str(i))
    outfile.write("\n")
    line=infile1.readline()
outfile.close()