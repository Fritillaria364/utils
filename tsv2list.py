import sys
import re
import pickle
from pyknp import Jumanpp

args = sys.argv

_ascii_re = re.compile(r'\A[\x00-\x7f]*\Z')
def isAscii(s):
    return isinstance(s,str) and _ascii_re.match(s)

with open(args[1],"r") as f:
    textslist = [ s.split("\t")[1].strip() for s in f if len(s.split("\t")) > 1]
with open(args[2],"r") as f:
    wordslist = [ s.split("\t")[1].strip() for s in f if len(s.split("\t")) > 1]

tlist = [ w.replace(" ","_") for w in textslist if w is not "" and not isAscii(w)]
wlist = [ w.replace(" ","_") for w in wordslist if w is not ""]

t_midasi = []
w_midasi = []

jumanpp = Jumanpp()
"""
for i,s in enumerate(tlist):
    print("Processing Text:{}".format(i))
    if s == "":
        continue
    result = jumanpp.analysis(s)
    midasi_lst = []
    for w in result.mrph_list():
        midasi_lst.append([w.midasi.replace("_"," "),"O"])
    t_midasi.append(midasi_lst)
"""
print("-----------------")

for i,s in enumerate(wlist):
    print("Processing Word:{}".format(i))
    if s == "":
        continue
    result = jumanpp.analysis(s)
    midasi_lst = []
    for w in result.mrph_list():
        midasi = w.midasi.replace("_","")
        if midasi == "":
            continue
        midasi_lst.append(midasi)
    w_midasi.append(midasi_lst)

"""
with open("./text_midasi.list","wb") as f:
    pickle.dump(t_midasi,f)
"""

with open("./word_midasi.list","wb") as f:
    pickle.dump(w_midasi,f)
