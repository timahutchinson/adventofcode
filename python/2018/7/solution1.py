import re
from collections import defaultdict
import string

# Read in instructions, parse into independent and dependent step
p = re.compile("(?<=[Ss]tep\s)(\w)")
with open("../../../data/2018/7/data.txt") as f:
    lines = [p.findall(line.strip()) for line in f.readlines()]

# Create a list of the requirements for each step
reqs = defaultdict(list)
for pair in lines:
    reqs[pair[1]].append(pair[0])

# Fill in the missing values (i.e., those without requirements)
for let in list(string.ascii_uppercase):
    if let not in dict(reqs).keys():
        reqs[let] = []

# Create a master list (that will form our solution) and a holding list
holding = []
master = []
while len(reqs.keys()) > 0:
    # Add steps with no requirements to holding list
    del_keys = []
    for key in reqs.keys():
        if len(reqs[key]) == 0:
            holding.append(key)
            del_keys.append(key)
    for key in del_keys:
        del reqs[key]
    # Sort the holding list
    holding = sorted(holding)
    # Add the lexicographically first step to the master list
    this_step = holding[0]
    master.append(this_step)
    # Remove that step from the requirements of all other steps
    for key in reqs.keys():
        try:
            reqs[key].remove(this_step)
        except ValueError:
            pass
    # Remove it from the holding list
    holding.remove(this_step)
    # Repeat until the reqs dictionary is empty

print(''.join(master))
