import sys, re, string

f = open("inquireraugmented.csv", "r")
tag = sys.argv[1]

linenum = 0
for l in f:
    l = l.strip()
    if linenum == 0:
        toks = l.split(",")
        index = toks.index(tag)
        linenum += 1
    elif linenum == 1:
        linenum += 1
    elif linenum > 1:
        toks = l.split(",")
        word = toks[0].lower().split("#")[0]
        if len(toks[index]) > 1:
            print word
    
