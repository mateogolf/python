import random
def coinToss():
    heads = 0
    tails = 0
    for i in range(5000):
        ranInt = round(random.random())
        print ranInt
        if ranInt == 1:
            string = "heads"
            heads+=1
        else:
            string = "tails"
            tails+=1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(i+1,string,heads,tails)

coinToss()