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
	def __init__(self):
		self.bingliu_pos = pickle.load(open("../pickledData/liu_pos.p", "r"))
		self.bingliu_neg = pickle.load(open("../pickledData/liu_neg.p", "r"))
		self.anew = pickle.load(open("../pickledData/anew.p", "r"))
		self.warriner = pickle.load(open("../pickledData/warriner.p", "r"))

	def annotateDiscreteLiu(self, word):
		if word in self.bingliu_pos:
			return 6
		elif word in self.bingliu_neg:
			return 4
		else:
			return 0

	def annotateWarriner(self, word):
		if word in self.warriner:
			return self.warriner[word]
		else:
			return 0

	def annotateAnew(self, word):
		if word in self.anew:
			return self.anew[word]
		else:
			return 0


	# This is the function that should be called externally
	def annotate(self, sentence, model="liu"):
		words = sentence.split()
		if model=="liu":
			values = [self.annotateDiscreteLiu(word) for word in words]
		elif model=="warriner":
			values = [self.annotateWarriner(word) for word in words]
		elif model=="anew":
			values = [self.annotateAnew(word) for word in words]
		else: # default
			values = [self.annotateDiscreteLiu(word) for word in words]
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
			colors.append("mediumred")
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


# temp

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")


result = {}
result['success'] = True
result['keys'] = ",".join(fs.keys())

d = {}
for k in fs.keys():
    d[k] = fs.getvalue(k)

result['message'] = ",".join(map(str, myAnnotator.annotate(d['param'], "anything")))
#result['message'] = d['param']
#result['message'] = len(colorPicker([4, 6]))
#d['param'].upper() 


result['data'] = d

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()

