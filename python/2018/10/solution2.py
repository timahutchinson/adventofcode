import sys
import re

import numpy as np
from scipy.spatial.distance import cdist


def is_neighbor(p1, p2):
    return abs(p1[0] - p2[0]) <= 1 | abs(p1[1] - p2[1]) <= 1


def count_has_neighbors(points):
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
    i += 1
    sys.stdout.write("\r%d" % i)
    points = time_step(points, vels)
    if count_has_neighbors(points) > (0.9 * npoints):
        break

xmin = min(points, key=lambda x: x[0])[0]
xmax = max(points, key=lambda x: x[0])[0] + 2
ymin = min(points, key=lambda x: x[1])[1]
ymax = max(points, key=lambda x: x[1])[1] + 2

print("")
newpoints = [list(point) for point in points]
for j in range(ymin-1, ymax+2):
    row = ""
    for i in range(xmin-1, xmax+2):
        if [i, j] in newpoints:
            row += "#"
        else:
            row += "."
    print(row)
