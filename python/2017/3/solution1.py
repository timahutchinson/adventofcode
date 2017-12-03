# The spiral is nested squares of odd side length.  First, find the size of the
# square the value is on.  Then, find the closest corner value.  Use the
# difference from the closest corner value to calculate the path length.
import math

import numpy as np

def calc_side_length(n):
    side_length = math.ceil(math.sqrt(n))
    if side_length % 2 == 0:
        return side_length + 1
    else:
        return side_length

def calc_closest_corner(n, side_length):
    corners = [side_length**2]
    for _ in range(3):
        corners.append(corners[-1] - (side_length - 1))
    corners = np.array(corners)
    closest_corner = corners[np.abs(n - corners).argmin()]
    return closest_corner

def calc_manhattan_distance(n, side_length, closest_corner):
    return side_length - np.abs(n - closest_corner) - 1

def main():
    n = 289326
    side_length = calc_side_length(n)
    closest_corner = calc_closest_corner(n, side_length)
    print "Solution is %d" % calc_manhattan_distance(n, side_length, closest_corner)

if __name__ == "__main__":
    main()
