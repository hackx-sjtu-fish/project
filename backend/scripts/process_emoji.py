from nltk.corpus import stopwords

english_stopwords = stopwords.words('english')

infile = file("emoji.csv","rb")
outfile = file("emoji_splitted.csv","wb")
line = infile.readline()

while line!="":
    tmp=line.replace('\n',"").split(',')
    outfile.write(tmp[0])
    tmp=tmp[1].split()+tmp[2].split('|')
    tmp2=[]
    for i in tmp:
        tmp2+=[j.replace(":","") for j in i.split(" ") if not j==""]
    tmp=tmp2
    tmp = [word for word in tmp if not unicode(word) in english_stopwords]
    tmp = list(set(tmp))
    for i in tmp:
        outfile.write(","+i)
    outfile.write("\n")
    line = infile.readline()

outfile.close()