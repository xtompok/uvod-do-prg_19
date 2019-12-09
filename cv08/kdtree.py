from point_generator import random_square, circle

N_POINTS = 10

sq = random_square(N_POINTS)

def kd_tree(points,axis):
    # axis = 'x' or 'y'
    # if len(points) == 1, only print point and return
    # sort points according to axis
    points.sort(key = lambda p: p[0]) # x axis
    points.sort(key = lambda p: p[1]) # y axis
    # split points to two halves - points0, points1
    # find and print coordinate of the middle point
    # print each half
    print("Axis {}: {}, before: {}, after: {}".format(
        axis,FIXME, points0, points1))
    # recurse on each half

print("Points: {}".format(sq))
kd_tree(sq,'x')