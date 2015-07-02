import pickle

posWords = [line.rstrip() for line in open('../lexicons/liu_positive-words.txt')]
negWords = [line.rstrip() for line in open('../lexicons/liu_negative-words.txt')]

pickle.dump(posWords, open("../pickledData/liu_pos.p", "wb"))
pickle.dump(negWords, open("../pickledData/liu_neg.p", "wb"))


# f = open('../lexicons/bradley_lang_anew_parsed.csv', 'r')
# allStrings = f.readline()
# thisDict = {} # dictionary that just links word to mean valence
# for line in allStrings.split():
# 	thisLine = line.split(",")
# 	thisDict[thisLine[0]] = float(thisLine[1])
# f.close()
# pickle.dump(thisDict, open("../pickledData/anew.p", "wb"))


f = open('../lexicons/warriner_valence.csv', 'r')
allStrings = f.readline()
thisDict = {} # dictionary that just links word to mean valence
for line in allStrings.split():
	thisLine = line.split(",")
	if len(thisLine)>1:
		thisDict[thisLine[0]] = float(thisLine[1])
f.close()
pickle.dump(thisDict, open("../pickledData/warriner_valence.p", "wb"))

f = open('../lexicons/warriner_arousal.csv', 'r')
allStrings = f.readline()
thisDict = {} # dictionary that just links word to mean valence
for line in allStrings.split():
	thisLine = line.split(",")
	if len(thisLine)>1:
		thisDict[thisLine[0]] = float(thisLine[1])
f.close()
pickle.dump(thisDict, open("../pickledData/warriner_arousal.p", "wb"))


f = open('../lexicons/Concreteness_ratings_Brysbaert_et_al_BRM_parsed.csv', 'r')
allStrings = f.readline()
thisDict = {} # dictionary that just links word to mean valence
for line in allStrings.split():
	thisLine = line.split(",")
	if len(thisLine)>1:
		thisDict[thisLine[0]] = float(thisLine[1])
f.close()
pickle.dump(thisDict, open("../pickledData/concreteness.p", "wb"))
