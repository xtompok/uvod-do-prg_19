from random import uniform


def random_square(npoints):
    """Returns list of tuples - random points in unit square."""
    points = []
    for _ in range(npoints):
        point = (uniform(0,1),uniform(0,1))
        points.append(point)
    return points


def circle(npoints):
    pass
