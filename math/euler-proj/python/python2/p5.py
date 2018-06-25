#Euler Problem 5. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def num_in_i(smallest, i):
    if smallest % i == 0:
        return True
    else:
        return False

def Finder(num):
    found = False
    smallest = num
    i = 1
    while found == False:
        while num_in_i(smallest, i) == True:
            if i == num:
                found = True
                return smallest
            i += 1
        i = 1
        smallest += num
        #print smallest

#print Finder(10)
