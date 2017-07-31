def printOdd1to1000():
    for i in range(1001):
        if i %2 != 0:
            print i
printOdd1to1000()

def printMult5to1000():
    for i in range(1001):
        if i %5 == 0:
            print i
printMult5to1000()
a = [1, 2, 5, 10, 255, 3]
def sumTest(arr):
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i]
    print sum

def avgTest(arr):
    sum = 0
    for i in range(1,len(arr)):
        sum += arr[i]
    print sum/len(arr)

sumTest(a)
avgTest(a)