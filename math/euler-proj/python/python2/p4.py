#Euler Project 4. Find the largest palindrome made by a product of two 3-digit numbers.
#Solved!

#Variables
x = 999
y = 999
z = 0
found = False
palindromes = []

#Defintions
def palindrome(num):
    global found
    found = (str(num) == str(num)[::-1])

def product(a, b):
    global z
    z = x*y

while x >= 100:
    #global found, x, y, z
    product(x,y)
    palindrome(z)
    if found == True:
        print x, y, z
        palindromes.append(z)
        y -= 1
        if y < 100:
            y = 998
            x -= 1
    elif found == False:
        y -= 1
        if y < 100:
            y = 998
            x -= 1
print max(palindromes)
