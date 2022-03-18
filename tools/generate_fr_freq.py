



f = open("words/lexique/Lexique383.tsv", "r")
contents = f.read()
f.close()
lines = contents.splitlines()

del lines[0]

L = len(lines)
print(L)
f = open("./fr_unigram_freq.csv", "w")
for i,l in enumerate(lines):
    if i%1000 == 0: print(i)
    ww = l.split("\t")
    f.write(ww[0]+","+str(int(float(ww[9])*100)))    
    f.write('\n')
f.close()
