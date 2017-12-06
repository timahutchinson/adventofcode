with open("../../../data/2017/5/data.txt", "rb") as f:
    vals = [int(line.replace('\n','')) for line in f.readlines()]

count = 0
ind = 0
while True:
    old_val = vals[ind]
    vals[ind] += 1
    count += 1
    ind += old_val
    if ind >= len(vals):
        break

print "Solution is %d" % count
