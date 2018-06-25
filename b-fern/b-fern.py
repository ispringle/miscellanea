import random
import matplotlib.pyplot as plt

def fern(array, iterations):
	for i in range(iterations):
		x = array[i][0]
		y = array[i][1]
		
		probability = random.random()
		if probability < 0.01:
			array.append(_func1(x, y))
		elif probability > 0.01 and probability < 0.85:
			array.append(_func2(x, y))
		elif probability > 0.05 and probability < 0.92:
			array.append(_func3(x, y))
		else:
			array.append(_func4(x, y))
	return array

def _func1(x, y):
	return [(0 * x), (0.16 * y)]

def _func2(x, y):
	return [(0.85 * x + 0.04 * y), (-0.04 * x + 0.85 * y + 1.60)]

def _func3(x, y):
	return [(0.20 * x - 0.26 * y), (0.23 * x + 0.22 * y + 1.60)]

def _func4(x, y):
	return [(-0.15 * x + 0.28 * y), (0.26 * x + 0.24 * y + 0.44)]

def plot(array):
	x = []
	y = []
	plt.xlabel("x")
	plt.ylabel("y")
	plt.title("Barnsley Fern")
	
	for i in range(len(array)):
		plt.scatter(array[i][0], array[i][1])
	plt.show()

array = [[0,0]]
plot(fern(array, 10000))


