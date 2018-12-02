from collections import Counter

import numpy as np

with open("../../../data/2018/2/data.txt") as f:
    lines = [line.strip() for line in f.readlines()]

twos = 0
threes = 0
for line in lines:
    if any(np.array(list(Counter(line).values())) == 2):
        twos += 1
    if any(np.array(list(Counter(line).values())) == 3):
        threes += 1

print(twos * threes)
