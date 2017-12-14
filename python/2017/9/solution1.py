import re

with open("../../../data/2017/9/data.txt", "rb") as f:
    stream = f.read().strip()

# First, remove all canceled characters
stream = re.sub('!.', '', stream)

# Next, all garbage
stream = re.sub('<[^>]*>', '', stream)

# Score groups
score = 0
value = 0
for char in stream:
    if char == '{':
        value += 1
    elif char == '}':
        score += value
        value -= 1
print "Solution is %d" % score
