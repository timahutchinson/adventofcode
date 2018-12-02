from itertools import combinations

import numpy as np

with open("../../../data/2018/2/data.txt") as f:
    lines = [np.array(list(line.strip())) for line in f.readlines()]

for pair in combinations(lines, 2):
    if sum(pair[0] == pair[1]) == (len(pair[0]) - 1):
        print(''.join(pair[0][pair[0] == pair[1]]))
        break
