from math import exp
import random

class Perceptron(object):
	def __init__(self, learning_rate=0.1, errors_satisfied=0, seed=0, random_init=False, bits=25, quadratic=False):			
		
		if random_init:
			random.seed(seed)
			self.weights = [random.uniform(-1,1)] * 2**bits
		else:
			self.weights = [0.] * 2**bits
		self.learning_rate = learning_rate
		self.errors_satisfied = 0
		self.random_init = False
		self.quadratic = quadratic
		self.X = []
		self.y = 0.
		self.error = 0.
		self.bits = 2**bits
		self.Prediction = 0.
		self.seed = seed
	
	def fit(self,c,sample_id,label):
		self.ID = sample_id
		self.y = float(label)
		f = c.split()
		self.X = [0.] * len(f)
		for i, token in enumerate(f):
			self.X[i] = hash(str(token)+str(self.seed)) % self.bits

	def predict(self):
		# Calculate dotproduct
		# Predicts 1 when activation threshold reached
		dotp = 0
		for i in self.X:
			dotp += self.weights[i]
		if dotp > 0:
			self.Prediction = 1
		else:
			self.Prediction = 0
		return self.Prediction
	
	def predict_proba(self):
		def zygmoid(x): 
			# Sigmoid function
			return 1 / (1 + exp(-x))
		dotp = 0
		for i in self.X:
			dotp += self.weights[i]
		return zygmoid(dotp / float(len(self.X)+1))

	def hard_error(self):
		# error is 1 if misclassified as 0, error is -1 if misclassified as 1
		error = self.y - self.Prediction
		self.error = error
		if error != 0:
			return 1
		else:
			return 0

	def update(self, prediction):
		for i in self.X:
			self.weights[i] += self.learning_rate * self.error

	def save(self,file_path):
		with open(file_path,"wb") as outfile:
			for k in self.weights:
				outfile.write("%s\n"%k)

	def load(self,file_path):
		w = []
		for e, line in enumerate(open(file_path)):
			w.append(float(line.strip()))
