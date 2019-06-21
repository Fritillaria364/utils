import sys

argvs = sys.argv

with open(argvs[1],"r") as f:
    wakati = []
    str = []
    for line in f:
        word = line.split()[0]
        if word in "*+#":
            continue
        elif word == "EOS":
            wakati.append(" ".join(str)+"\n")
            str = []
            continue
        str.append(word)

with open(argvs[2],"w") as f:
    [ f.write(w) for w in wakati]
