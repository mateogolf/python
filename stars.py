import numbers
def draw_stars(arr):
    for starCount in arr:
        string = ""
        for i in range(starCount):
            string += "*"
        print string
x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

def draw_stars2(arr):
    for starCount in arr:
        string = ""
        if type(starCount) is str:
            for i in range(len(starCount)):
                string += starCount[0].lower()
            print string
        elif isinstance(starCount,numbers.Number):
            for i in range(starCount):
                string += "*"
            print string

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)