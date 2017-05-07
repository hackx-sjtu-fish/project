infile=file("emoji_num.csv","rb")
outfile1=file("emoji_keywords_id.json","wb")
outfile2=file("emoji_unicode.json","wb")

list = []
list2 = []

line = infile.readline()

while line!="":
    tmp=[]
    for i in line.replace("\n","").replace("\r","").split(",")[1:]:
        tmp.append(int(i))
    list2.append(tmp)

    list.append(line.replace("\n","").replace("\r","").split(",")[0])
    line = infile.readline()

outfile2.write(json.dumps(list))
outfile2.close()

outfile1.write(json.dumps(list2))
outfile1.close()