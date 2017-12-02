triangles = []

with open('input.txt', 'rb') as f:
    for line in f:
        triangles.append(line.strip().split())

count = 0

for tri in triangles:
    tri = map(int, tri)
    if (tri[0] + tri[1] > tri[2]):
        if (tri[0] + tri[2] > tri[1]):
            if (tri[1] + tri[2] > tri[0]):
                print tri
                count += 1

print "Total valid triangles:  %s" % count
