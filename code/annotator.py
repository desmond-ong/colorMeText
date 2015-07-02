#!/usr/bin/python
# Sentiment Functions
import pickle

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

	# def annotateAnew(self, word):
	# 	if word in self.anew:
	# 		return self.anew[word]
	# 	else:
	# 		return 0

	# scale from 1-5 to 1-9
	def annotateConcrete(self, word):
		self.concreteness = pickle.load(open("../pickledData/concreteness.p", "r"))
		if word in self.concreteness:
			return ((self.concreteness[word]-1)*2 + 1)
		else:
			return 0

	# This is the function that should be called externally
	def annotate(self, sentence, model="liu"):
		words = sentence.split()
		#if model=="polarity":
		#	values = [self.annotateDiscreteLiu(word) for word in words]
		if model=="valence":
			values = [self.annotateWarrinerValence(word) for word in words]
		elif model=="arousal":
			values = [self.annotateWarrinerArousal(word) for word in words]
		elif model=="concreteness":
			values = [self.annotateConcrete(word) for word in words]
		else: # default
			values = [self.annotateDiscreteLiu(word) for word in words]
		return values
