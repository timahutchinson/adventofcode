from collections import Counter

with open("../../../data/2017/11/data.txt", "rb") as f:
    steps = f.read().strip().split(',')

counts = Counter(steps)

pairs = {
         ('s', 'n'):None,
         ('nw', 'se'):None,
         ('ne', 'sw'):None,
         ('se', 'sw'):'s',
         ('ne', 'nw'):'n',
         ('ne', 's'):'se',
         ('nw', 's'):'sw',
         ('se', 'n'):'ne',
         ('sw', 'n'):'nw'
         }

for pair in pairs:
    print pair
    print counts
    print ''
    diff = abs(counts[pair[0]] - counts[pair[1]])
    if (counts[pair[0]] != 0) & (counts[pair[1]] != 0):
        if counts[pair[0]] >= counts[pair[1]]:
            counts[pair[0]] -= counts[pair[1]]
            counts[pair[1]] -= counts[pair[1]]
        else:
            counts[pair[1]] -= counts[pair[0]]
            counts[pair[0]] -= counts[pair[0]]
        if pairs[pair] is not None:
            counts[pairs[pair]] += diff
