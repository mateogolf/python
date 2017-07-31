def checkerboard():
    for i in range(1,9):
        string = ""
        if i % 2 != 0:
            for j in range(4):
                string += "* "
            print string
        else:
            for k in range(4):
                string += " *"
            print string

checkerboard()