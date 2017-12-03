from itertools import combinations

with open('../../../data/2017/2/data.txt', 'rb') as f:
    rows = [map(int, row.strip().split('\t')) for row in f.readlines()]

total = 0
for row in rows:
    for pair in combinations(row,2):
        if max(pair) % min(pair) == 0:
            total += max(pair) / min(pair)
        else:
            pass

print "Solution is %d" % total
