# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
# DIST = 100
# for x in range(0,6): #Creates 6 boxes
#     print "x", x
#     for y in range(1,5): #Draws each side of the box length of DIST
#         print "y", y
#         # turn the pointer 90 degrees to the right
#         turtle.right(90) #turns right to make a box
#         # advance according to set distance
#         turtle.forward(DIST)
#     # add to set distance
#     DIST += 20
#CREATE A PACMAN
radius = 50
turtle.circle(-(radius),225)
turtle.right(90)
turtle.forward(radius)
turtle.right(270)
turtle.forward(radius)
turtle.right(90)
turtle.circle(-(radius),45)
