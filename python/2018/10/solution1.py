import re
from sys import stdout

import numpy as np
from scipy.spatial.distance import cdist


def is_neighbor(p1, p2):
    return abs(p1[0] - p2[0]) <= 1 | abs(p1[1] - p2[1]) <= 1


def count_has_neighbors(points):
    '''count = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if is_neighbor(points[i], points[j]):
                count += 1
                break
    return count * 2'''
    count = 0
    npoints = points.shape[0]
    for i, point in enumerate(points):
        inds = np.array([True] * npoints)
        inds[i] = False
        count += (cdist(np.array([point]), points[inds])[0] < 2).any()
    return count


def time_step(points, vels):
    return points + vels


with open("../../../data/2018/10/data.txt") as f:
    p = re.compile("\w+=<([\d\s-]+),\s([\d\s-]+)>\s\w+=<([\d\s-]+),\s([\d\s-]+)>")
    lines = [list(map(int, p.findall(line.strip())[0])) for line in f.readlines()]
    points = np.array([val[:2] for val in lines])
    vels = np.array([val[2:] for val in lines])

npoints = points.shape[0]
i = 0
while True:
    stdout.write("\r%d" % i)
    if count_has_neighbors(points) > (0.5 * npoints):
        break
    points = time_step(points, vels)
    i += 1
