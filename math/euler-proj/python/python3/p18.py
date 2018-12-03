Triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

Triangle2 = [           #Test, answer is 3, 7, 4, 9
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]

sum = 0
path = []
row = 0
num = 0

sums = []


#These are the "greedy" functions
def add(Matrix, x, y):
    global sum
    sum += Matrix[x][y]
    path.append(Matrix[x][y])

def next(Matrix):
    global num, row
    if Matrix[row+1][num] > Matrix[row+1][num+1]:
        add(Matrix, row+1, num)
        row+= 1
    else:
        add(Matrix, row+1, num+1)
        row += 1
        num += 1

def greedy(Matrix):
    add(Matrix, num, row) #initializes path[] and sum with Matrix[0][0]
    for i in range(len(Matrix)-1):
        next(Matrix)
    print(sum)
    print(path)

#These are the Dynamic Programming functions
def add_next(Matrix, row):
    i = 0
    for i in range(len(sums)):
        if i == sums[0]:
            sums[0] = sums[0] + Matrix[row][0]
        elif i == sums[-1]:
            sums[-1] = sums[-1] + Matrix[row][-1]
        else:
            sums[i] = sums[i] + Matrix



def bottoms_up(Matrix):
    #sums = Matrix[-1]
    i = 0
    for i in range(len(Matrix[-1])):
        if i == 0:
            sums.append(Matrix[-1][i])
        elif i == (len(Matrix[-1]) - 1):
            sums.append(Matrix[-1][i])
        else:
            sums.append(Matrix[-1][i])
            sums.append(Matrix[-1][i])

def test(matrix):
	for row in range(len(matrix) - 1, 0, -1):
		for col in range(0, row):
			matrix[row -1][col] += max(matrix[row][col], matrix[row][col+1])
	return matrix[0][0]

print(test(Triangle))
			
