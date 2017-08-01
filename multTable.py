def printMultTable():
    for i in range(13):
        if i == 0:
            print "x   1  2  3  4  5  6  7  8   9  10  11  12"
        else:
            string = str(i) + "  "
            for col in range(1,13):
                string += str(i*col) + "  "
            print string

printMultTable()