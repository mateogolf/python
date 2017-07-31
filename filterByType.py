sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def filterByType(val):
    print val
    #If integer, 
    if type(val) is int:
        if(val >= 100):# >=100 print "That's a big number!"
            print "That's a big number!"
        elif(val < 100): #<100 print "That's a small number"
            print "That's a small number"
    #if string
    elif type(val) is str:
        if(len(val) >= 50):#str>= 50 chars print "Long sentence."
            print "Long sentence"
        elif(len(val) < 50): #<50 chars print "short sentence"
            print "Short sentence"
    #If List
    elif type(val) is list:
        if(len(val) >= 10):#length>= 10 print "Long sentence."
            print "Big List!"
        elif(len(val) < 10): #<10 chars print "short sentence"
            print "Short List."

filterByType(sI)
filterByType(mI)
filterByType(bI)
filterByType(eI)
filterByType(spI)
filterByType(sS)
filterByType(mS)
filterByType(bS)
filterByType(eS)
filterByType(aL)
filterByType(mL)
filterByType(lL)
filterByType(eL)
fiterByType(spL)