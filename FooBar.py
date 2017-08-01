import math
def fooBar():
    for num in range(101,10001):
        print num
        isPrime = True
        if num == 1:
            isPrime = False
        for i in range(2,num): #checks for prime
            if num%i == 0:
                isPrime = False
                break
        if isPrime:
            print "Foo"
        else:
            #Check for perfect square
            sqRoot = math.sqrt(num)
            intSQRT = int(sqRoot)
            if (sqRoot-intSQRT) == 0:
                print "Bar"
            else: #Neither
                print "FooBar"


fooBar()