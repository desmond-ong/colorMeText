# Sentiment Functions
import pickle

class SentimentAnnotator():
	def __init__(self):
		self.bingliu_pos = pickle.load(open("../pickledData/liu_pos.p", "r"))
		self.bingliu_neg = pickle.load(open("../pickledData/liu_neg.p", "r"))
		self.anew = pickle.load(open("../pickledData/anew.p", "r"))
		self.warriner = pickle.load(open("../pickledData/warriner.p", "r"))

	def annotateDiscreteLiu(self, word):
		if word in self.bingliu_pos:
			return 9
		elif word in self.bingliu_neg:
			return 1
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
