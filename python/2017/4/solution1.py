with open("../../../data/2017/4/data.txt", "rb") as f:
    lines = [line.replace('\n','').split() for line in f.readlines()]

count = 0
for line in lines:
    if len(set(line)) == len(line):
        count += 1

print "Solution is %i" % count
