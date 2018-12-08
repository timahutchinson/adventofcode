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

# Create a dictionary of required time per job
times = {val[0]: val[1] for val in
         zip(list(string.ascii_uppercase), list(range(61, 87)))}

# Create a dictionary of workers to hold their current step and time spent
workers = {i: [None, 0] for i in range(1, 6)}

# Create a holding list for ready tasks
holding = []
t = 0
while (len(reqs.keys()) > 0) or any([val[0] for val in workers.values()]):
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
    # Assign as many tasks as possible to free workers
    del_tasks = []
    for task in holding:
        for key in workers.keys():
            if not workers[key][0]:
                workers[key][0] = task
                workers[key][1] = 1
                del_tasks.append(task)
                break
    for task in del_tasks:
        holding.remove(task)
    # Check to see if any tasks being worked are finished
    # If so, free them, and remove the task from the requirements dict
    for key in workers.keys():
        if workers[key][0]:
            if workers[key][1] == times[workers[key][0]]:
                this_step = workers[key][0]
                for key2 in reqs.keys():
                    try:
                        reqs[key2].remove(this_step)
                    except ValueError:
                        pass
                workers[key][0] = None
            # If they aren't finished, add a second to the time spent
            else:
                workers[key][1] += 1
    t += 1
    # Repeat until the reqs dictionary is empty

print(t)
