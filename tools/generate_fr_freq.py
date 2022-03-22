import re


f = open("words/lexique/Lexique383.tsv", "r")
contents = f.read()
f.close()
lines = contents.splitlines()

del lines[0]

L = len(lines)
print(L)

w2c = {}

for i, l in enumerate(lines):
    if i % 1000 == 0:
        print(i)
    ww = l.split("\t")

    accented = ww[0]
    no_accent = accented.lower()
    no_accent = re.sub(r"[àáâãäå]", "a", no_accent)
    no_accent = re.sub(r"[èéêë]", "e", no_accent)
    no_accent = re.sub(r"[ìíîï]", "i", no_accent)
    no_accent = re.sub(r"[òóôõö]", "o", no_accent)
    no_accent = re.sub(r"[ùúûü]", "u", no_accent)
    no_accent = re.sub(r"[ç]", "c", no_accent)

    count = int(float(ww[9]) * 100)

    w2c[no_accent] = count + w2c.get(no_accent, 0)

f = open("./fr_unigram_freq.csv", "w")
for k, v in w2c.items():
    f.write(k + "," + str(v))
    f.write("\n")
f.close()
