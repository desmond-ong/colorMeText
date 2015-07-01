import pickle

posWords = [line.rstrip() for line in open('../lexicons/liu_positive-words.txt')]
negWords = [line.rstrip() for line in open('../lexicons/liu_negative-words.txt')]

pickle.dump(posWords, open("../pickledData/liu_pos.p", "wb"))
pickle.dump(negWords, open("../pickledData/liu_neg.p", "wb"))


f = open('../lexicons/bradley_lang_anew_parsed.csv', 'r')
allStrings = f.readline()
anew_dict = {} # dictionary that just links word to mean valence
for line in allStrings.split():
	thisLine = line.split(",")
	anew_dict[thisLine[0]] = thisLine[1]
f.close()

pickle.dump(anew_dict, open("../pickledData/anew.p", "wb"))