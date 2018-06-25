#Euler Problem 5. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

found = False
a1 = False
a2 = False
a3 = False
a4 = False
a5 = False
a6 = False
a7 = False
a8 = False
a9 = False
a10 = False

def Finder(num):
    #global num
    while found == False:
        global a1
        a1 == False
        global a2
        a2 == False
        global a3
        a3 == False
        global a4
        a4 == False
        global a5
        a5 == False
        global a6
        a6 == False
        global a7
        a7 == False
        global a8
        a8 == False
        global a9
        a9 == False
        global a10
        a10 == False
        #print num
        if num % 1 == 0:
            a1 == True
        if num % 2 == 0:
            a2 == True
        if num % 3 == 0:
            a3 == True
        if num % 4 == 0:
            a4 == True
        if num % 5 == 0:
            a5 == True
        if num % 6 == 0:
            a6 == True
        if num % 7 == 0:
            a7 == True
        if num % 8 == 0:
            a8 == True
        if num % 9 == 0:
            a9 == True
        if num % 10 == 0:
            a10 == True
        if (a1 == True and a1 == True and a2 == True and a3 == True and
                a4 == True and a5 == True and a6 == True and a7 == True and
                    a8 == True and a9 == True and a10 == True):
            print num
        else:
            num +=1
            print num

Finder(1)
