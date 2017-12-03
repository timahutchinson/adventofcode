# Let's do this the brute force way - build the spiral step by step
# until a value appears that's greater than our input.
import numpy as np

def main():
    n = 289326
    spiral = np.zeros((11,11)) # Size arbitrary, as long as it's big enough
    pos = [5,5]
    spiral[pos[0],pos[1]] = 1
    horizdir = 1
    vertdir = 1
    steps = 1
    while steps <= 10:
        for step in xrange(steps):
            pos[0] += horizdir
            num = np.sum([
                          spiral[pos[0]-1, pos[1]],
                          spiral[pos[0]+1, pos[1]],
                          spiral[pos[0], pos[1]+1],
                          spiral[pos[0], pos[1]-1],
                          spiral[pos[0]+1, pos[1]+1],
                          spiral[pos[0]+1, pos[1]-1],
                          spiral[pos[0]-1, pos[1]+1],
                          spiral[pos[0]-1, pos[1]-1],
                          ])
            if num > n:
                print "Solution is %d" % num
                return
            else:
                spiral[pos[0], pos[1]] = num
        for step in xrange(steps):
            pos[1] += vertdir
            num = np.sum([
                          spiral[pos[0]-1, pos[1]],
                          spiral[pos[0]+1, pos[1]],
                          spiral[pos[0], pos[1]+1],
                          spiral[pos[0], pos[1]-1],
                          spiral[pos[0]+1, pos[1]+1],
                          spiral[pos[0]+1, pos[1]-1],
                          spiral[pos[0]-1, pos[1]+1],
                          spiral[pos[0]-1, pos[1]-1],
                          ])
            if num > n:
                print "Solution is %d" % num
                return num
            else:
                spiral[pos[0], pos[1]] = num
        steps += 1
        horizdir *= -1
        vertdir *= -1

if __name__ == "__main__":
    main()
