import re
import random

with open("../../../data/2017/7/data.txt", "rb") as f:
    lines = [re.split(" *-> *", re.sub("\(\d+\)", "", line)) for line in f.readlines()]
    lines = [map(lambda x: x.strip().split(', '), line) for line in lines]

ind = random.randint(0,len(lines))
program = lines[ind][0][0]
stop = False
while not stop:
    stop = True
    for line in lines:
        try:
            if program in line[1]:
                program = line[0][0]
                stop = False
                break
        except IndexError:
            pass

print "Solution is %s" % program
