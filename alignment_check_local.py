""

import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input","-i")
parser.add_argument("--alignment_file","-a")

args = parser.parse_args()

with open(args.input,"r") as f:
    concat_sent = [ ln for ln in f]

with open(args.alignment_file,"r") as f:
    align = [ ln.split() for ln in f]

j_sents = []
e_sents = []

for s in concat_sent:
    s1,s2 = re.sub(r" \|\|\| ","|", s).split("|")
    e_sents.append(s1)
    j_sents.append(s2)

for i,align_set in enumerate(align):
    print("---------Sent {} alignment--------".format(i))
    print(e_sents[i])
    print(j_sents[i])
    e_words = e_sents[i].split()
    j_words = j_sents[i].split()
    for a in align_set:
        ind1,ind2 = a.split("-")
        print("{} - {}".format(e_words[int(ind1)],j_words[int(ind2)]))
    print("----------------------------------")