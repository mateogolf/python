import random
scores = []
for i in range(10):
    random_grade = random.randint(60,100)
    scores.append(random_grade)
print scores

def grades(arr):
    print "Scores and Grades"
    for i in arr:
        if i < 60:
            print "ERROR"
            return
        elif i >= 60 and i <70:
            grade = "D"
        elif i >= 70 and i <80:
            grade = "C"
        elif i >= 80 and i <90:
            grade = "B"
        elif i >= 90 and i <=100:
            grade = "A"
        print "Scores: {}; Your grade is {}".format(i,grade)
    print "End of Program. BYE!"
    
grades(scores)