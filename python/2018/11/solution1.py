import numpy as np
from scipy.signal import convolve2d


def power_level(coord, serial):
    return (((((coord[0] + 10) * coord[1]) + serial) * (coord[0] + 10)) // 100 % 10) - 5


def build_grid(size, serial):
    return [[power_level((i, j), serial) for i in range(1, size+1)] for j in range(1, size+1)]


with open("../../../data/2018/11/data.txt") as f:
    serial = int(f.read().strip())

grid = build_grid(300, serial)
total_powers = convolve2d(np.array(grid), np.ones(shape=(3, 3)), mode="same")

print(tuple(reversed(np.unravel_index(total_powers.argmax(), total_powers.shape))))
