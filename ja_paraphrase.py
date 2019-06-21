import MeCab
import sys
import csv

#   0      1     2     3   4   5      6       7     8      9
# 表層形 / POS / POS2 / * / * / * / 動詞活用 / 原形 / 読み / 読み2
def sent_analyze(sent,tagger):
    raw_analysis = tagger.parse(sent).replace("\t",",").split("\n")[:-2]
    analyzeList = [ raw.split(",") for raw in raw_analysis ]
    return analyzeList

def convert( word, form, verbList):
    for row in verbList:
        if word == row[10]: #品詞発見
            if form in row[9]: #活用発見
                return row[0]

args = sys.argv

with open(args[1],"r") as f:
    ja_docs = f.readlines()

with open("~/corpus/csv/Verb.csv") as verb:
    verbList = csv.reader(verb)

stopChars = ["。","、","?","!","！","？","｡","､"]
delWords = ["です","ます","でし","まし"]
mtag = MeCab.Tagger()

f = open(args[2],"w")
for jsent in ja_docs:

    ja_analysis = sent_analyze(jsent,mtag)
    wakati_sents = []
    for i,w in enumerate(ja_analysis):
        if w[0] in delWords:
            if w[0] == "です":
                wakati_sents.append("だ")
            elif w[0] == "でし":
                wakati_sents.append("だっ")
            elif w[0] == "ます" and i > 0:
                wakati_sents[-1] = ja_analysis[i-1][-3]
                continue
            elif w[0] == "まし" and i > 0:
                if "五段" in w[6]:
                    wakati_sents.append(convert(w[-3],"連用タ接続",verbList))
                else:
                    continue
        elif w[1] == "助詞" and i < len(ja_analysis) and ja_analysis[i+1] in stopChars:
            continue
        else:
            wakati_sents.append(w[0])

    f.write(" ".join(wakati_sents))

f.close()