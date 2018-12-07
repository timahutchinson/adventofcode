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
nearest = np.argmin(dists, axis=0)
min_dists = np.min(dists, axis=0)
nearest[(dists == min_dists).sum(axis=0) > 1] = len(points) + 1
nearest = nearest.reshape(np.meshgrid(np.arange(xmin, xmax),
                          np.arange(xmin, xmax))[0].shape)
ignore_id = np.unique(np.vstack([nearest[0], nearest[-1], nearest[:, 0],
                                 nearest[:, -1]]))
nearest[np.isin(nearest, ignore_id)] = len(points) + 1

print(np.max(np.bincount(nearest.ravel())[:-1]))
