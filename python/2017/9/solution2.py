import re

with open("../../../data/2017/9/data.txt", "rb") as f:
    stream = f.read().strip()

# Removed canceled characters
stream = re.sub('!.', '', stream)

# Capture each instance of garbage
garbages = re.findall('<[^>]*>', stream)

ngarbage = 0
for garbage in garbages:
    ngarbage += len(garbage) - 2

print "Solution is %d" % ngarbage
