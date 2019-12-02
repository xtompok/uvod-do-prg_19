from turtle import speed, forward,backward, left, right, exitonclick
from random import randrange, uniform

def tree(length, minangle, maxangle):
    if length < 10:
        return
    # select random angle from range
    angle = randrange(minangle,maxangle)
    # select random *new length* from range
    new_length = length*uniform(0.5,0.8)

    # Go forward for length
    forward(length)

    # rotate by angle
    left(angle)
    # draw subtree
    tree(new_length,minangle,maxangle)
    # rotate back
    right(angle)

    # rotate on the other side
    right(angle)
    # draw subtree
    tree(new_length,minangle,maxangle)
    # rotate back
    left(angle)
    # go back
    backward(length)
    return


left(90)
tree(100,30,70)
exitonclick()
