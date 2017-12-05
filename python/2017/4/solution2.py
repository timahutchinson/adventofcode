with open("../../../data/2017/4/data.txt", "rb") as f:
    lines = [line.replace('\n','').split() for line in f.readlines()]

count = 0
for line in lines:
    invalid = False
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if set(list(line[i])) == set(list(line[j])):
                invalid = True
    if not invalid:
        count += 1

print "Solution is %d" % count
