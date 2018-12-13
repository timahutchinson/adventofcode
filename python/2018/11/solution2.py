import numpy as np
from scipy.signal import convolve2d


def power_level(coord, serial):
    return (((((coord[0] + 10) * coord[1]) + serial) * (coord[0] + 10)) // 100 % 10) - 5


def build_grid(size, serial):
    return [[power_level((i, j), serial) for i in range(1, size+1)] for j in range(1, size+1)]


with open("../../../data/2018/11/data.txt") as f:
    serial = int(f.read().strip())

#serial = 42

max_power = 0
max_ind = None
max_n = None
grid = build_grid(300, serial)
for n in range(1, 51):
    total_powers = convolve2d(np.array(grid), np.ones(shape=(n, n)), mode="same")
    if total_powers.max() > max_power:
        max_power = total_powers.max()
        max_ind = tuple(reversed(np.unravel_index(total_powers.argmax(), total_powers.shape)))
        max_n = n

print("%d, %d, %d" % (max_ind[0] - max_n/2 + 1, max_ind[1] - max_n/2 + 1, max_n))
