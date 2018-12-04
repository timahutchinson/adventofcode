import re

import numpy as np

with open("../../../data/2018/3/data.txt") as f:
    lines = [re.findall("^#\d+ @ (\d+,\d+): (\d+x\d+)\n$", line)[0]
             for line in f.readlines()]

fabric = np.zeros(shape=(1000, 1000))
for line in lines:
    corner = tuple(map(int, line[0].split(",")))
    size = tuple(map(int, line[1].split("x")))
    fabric[corner[0]:corner[0] + size[0], corner[1]:corner[1] + size[1]] += 1

print(np.sum(fabric >= 2))
