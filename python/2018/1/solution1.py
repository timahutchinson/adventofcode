import numpy as np

with open("../../../data/2018/1/data.txt") as f:
    dfreqs = [line.strip() for line in f.readlines()]

print(np.cumsum(list(map(int, dfreqs)))[-1])
