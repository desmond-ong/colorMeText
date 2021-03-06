#!/usr/bin/python

#import cgi, cgitb,requests, re

#cgitb.enable()
#form = cgi.FieldStorage()
#print form.getvalue("data")


#def returnColors(text):
#    return ["blue", "green"]

import sys, string
import json
import cgi
import pickle
#from annotator import SentimentAnnotator
#from colorPicker import colorPicker

fs = cgi.FieldStorage()


class SentimentAnnotator():
	#def __init__(self):
		#self.anew = pickle.load(open("../pickledData/anew.p", "r"))
		

	def annotateDiscreteLiu(self, word):
		self.bingliu_pos = pickle.load(open("../pickledData/liu_pos.p", "r"))
		self.bingliu_neg = pickle.load(open("../pickledData/liu_neg.p", "r"))
		if word in self.bingliu_pos:
			return 6
		elif word in self.bingliu_neg:
			return 4
		else:
			return 0

	def annotateWarrinerValence(self, word):
		self.warrinerValence = pickle.load(open("../pickledData/warriner_valence.p", "r"))
		if word in self.warrinerValence:
			return self.warrinerValence[word]
		else:
			return 0

	def annotateWarrinerArousal(self, word):
		self.warrinerArousal = pickle.load(open("../pickledData/warriner_arousal.p", "r"))
		if word in self.warrinerArousal:
			return self.warrinerArousal[word]
		else:
			return 0

	def annotateConcrete(self, word):
		self.concreteness = pickle.load(open("../pickledData/concreteness.p", "r"))
		if word in self.concreteness:
			return ((self.concreteness[word]-1)*2 + 1)
		else:
			return 0

	# This is the function that should be called externally
	def annotate(self, sentence, model="valence"):
		words = sentence.split()
		#if model=="polarity":
			#values = [self.annotateDiscreteLiu(word.lower().strip()) for word in words]
		if model=="valence":
			values = [self.annotateWarrinerValence(word.lower().strip()) for word in words]
		elif model=="arousal":
			values = [self.annotateWarrinerArousal(word.lower().strip()) for word in words]
		elif model=="concreteness":
			values = [self.annotateConcrete(word.lower().strip()) for word in words]
		else: # default
			values = [self.annotateDiscreteLiu(word.lower().strip()) for word in words]
		return values


def colorPicker(scores):
	colors = []
	for score in scores:
		if score == 0 or score == 5:
			colors.append("gray")
		elif score < 5 and score > 4:
			colors.append("#FF5050")
		elif score <= 4 and score > 3:
			colors.append("red")
		elif score <= 3 and score > 2:
			colors.append("#800000")
		elif score <= 2 and score >= 1:
			colors.append("darkred")
		elif score < 6 and score > 5:
			colors.append("#3366FF")
		elif score <= 7 and score >= 6:
			colors.append("blue")
		elif score <= 8 and score > 7:
			colors.append("mediumblue")
		elif score <= 9 and score >= 8:
			colors.append("darkblue")
	return colors

myAnnotator = SentimentAnnotator()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

numberValues = myAnnotator.annotate(d['param'], d['lexicon'])
result['message'] = ",".join(colorPicker(numberValues))
#result['message'] = d['param']
#result['message'] = len(colorPicker([4, 6]))
#d['param'].upper() 


forMean = [5 if x==0 else x for x in numberValues]
result['mean'] = format((((sum(forMean)/len(forMean))-5)/4), '.2f')

result['colors'] = colorPicker(numberValues)

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

