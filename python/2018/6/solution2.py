import numpy as np
from scipy.spatial import distance

with open("../../../data/2018/6/data.txt") as f:
    points = [tuple(map(int, line.strip().replace(",", "").split()))
              for line in f.readlines()]

xmin = min(points, key=lambda x: x[0])[0]
xmax = max(points, key=lambda x: x[0])[0]
ymin = min(points, key=lambda x: x[1])[1]
ymax = max(points, key=lambda x: x[1])[1]

grid = np.dstack(np.meshgrid(np.arange(xmin, xmax),
                 np.arange(xmin, xmax))).reshape(-1, 2)
dists = distance.cdist(points, grid, metric='cityblock')
sum_dists = dists.sum(axis=0)

print(np.where(sum_dists < 10000, 1, 0).sum())
