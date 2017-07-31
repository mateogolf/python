def compareList(list_one,list_two):
    if len(list_one) != len(list_two):
        print "The lists are not the same."
        return
    for i in range(0,len(list_one)):
        first = list_one[i]
        second = list_two[i]
        if(first != second):
            print "The lists are not the same."
            return

    print "The lists are the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compareList(list_one,list_two)
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compareList(list_one,list_two)
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compareList(list_one,list_two)
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
compareList(list_one,list_two)