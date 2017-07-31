import numbers
def typeList(arr):
    firstType = type(arr[0])
    isMixed = False
    newStr = ""
    sumOf = 0
    for i in arr:
        if type(i) != firstType:
            isMixed = True
        if type(i) != str and not isinstance(i,numbers.Number):
            print "ERROR. function stopped"
            return
        if type(i) is str:
            newStr += i + " "
        elif type(int(i)) is int:
            sumOf += i
            # print str(sumOf)

    if isMixed:
        print "The list you entered is of mixed type"
        print "String: " + newStr
        print "Sum: " + str(sumOf)
    elif firstType is int:
        print "The list you entered is of integer type"
        print "Sum: " + str(sumOf)
    elif firstType is str:
        print "The list you entered is of string type"
        print "String: " + newStr

list1 = ['magical unicorns',[19,2],'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']
typeList(list1)
typeList(list2)
typeList(list3)