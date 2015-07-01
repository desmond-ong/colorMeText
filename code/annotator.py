# Sentiment Functions
import pickle

class SentimentAnnotator():
	def __init__(self):
		self.bingliu_pos = pickle.load(open("../pickledData/liu_pos.p", "r"))
		self.bingliu_neg = pickle.load(open("../pickledData/liu_neg.p", "r"))
		self.anew = pickle.load(open("../pickledData/anew.p", "r"))

	def annotateDiscrete(self, word):
		if word in self.bingliu_pos:
			return "pos"
		elif word in self.bingliu_neg:
			return "neg"
		else:
			return "neu"

	def annotateContinuous(self, word):
		if word in self.anew:
			return self.anew[word]-4.5
		else:
			return 0

	def annotate(self, sentence, model="Liu"):
		words = sentence.split()
		if model=="Liu":
			values = [self.annotateDiscrete(word) for word in words]
		else:
			values = [self.annotateContinuous(word) for word in words]
		return values

	def annotateSentence(self, sentence):
		return 0