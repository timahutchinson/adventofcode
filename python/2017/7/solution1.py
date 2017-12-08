import re
import random

with open("../../../data/2017/7/data.txt", "rb") as f:
    lines = [map(lambda x: x.strip().split(', '), re.split(" *-> *", re.sub("\(\d+\)", "", line.strip()))) for line in f.readlines()]

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
