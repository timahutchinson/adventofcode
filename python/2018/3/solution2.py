import re

import numpy as np

with open("../../../data/2018/3/data.txt") as f:
    lines = [re.findall("^(#\d+) @ (\d+,\d+): (\d+x\d+)\n$", line)[0]
             for line in f.readlines()]

for line in lines:
    fabric = np.zeros(shape=(1000, 1000))
    for line2 in lines:
        if line[0] != line2[0]:
            corner = tuple(map(int, line2[1].split(",")))
            size = tuple(map(int, line2[2].split("x")))
            fabric[corner[0]:corner[0] + size[0],
                   corner[1]:corner[1] + size[1]] += 1
    id = line[0]
    corner = tuple(map(int, line[1].split(",")))
    size = tuple(map(int, line[2].split("x")))
    if not any(fabric[corner[0]:corner[0] + size[0],
                      corner[1]:corner[1] + size[1]].flatten()):
        print(id)
        break
