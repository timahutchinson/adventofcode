tri1 = []
tri2 = []
tri3 = []

with open('input.txt', 'rb') as f:
    for i,line in enumerate(f):
        if (i % 3 == 0):
            tri1.append(map(int,line.strip().split()))
        elif (i % 3 == 1):
            tri2.append(map(int,line.strip().split()))
        elif (i % 3 == 2):
            tri3.append(map(int,line.strip().split()))

count = 0

for i,tri in enumerate(tri1):
    for j in xrange(3):
        if (tri[j] + tri2[i][j] > tri3[i][j]):
            if (tri[j] + tri3[i][j] > tri2[i][j]):
                if (tri2[i][j] + tri3[i][j] > tri[j]):
                    count += 1

print "Total valid triangles:  %s" % count
