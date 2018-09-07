'''
Calculate the Recaman Sequence to the _nth_ digit.
By Ian S. Pringle
GPLv3
'''

class sequence():
	
	def __init__(self):
		self.sequence = []
	
	def getN(self, nth):
		a = 0
		for n in range(1, nth + 1):
			if a - n > 0 and a - n not in self.sequence:
				self.sequence.append(a - n)
				a -= n
			else:
				self.sequence.append(a + n)
				a += n

