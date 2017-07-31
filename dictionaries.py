me = {
    'name': "Matt",
    'age': 28,
    'country of birth': "United States",
    'favorite language': "Python"
}
def printMe(obj):
    for key,data in obj.iteritems():
        print "My {} is {}".format(key,data)

printMe(me)