from operator import itemgetter

with open("../../../data/2019/3/data.txt") as f:
    steps = [line.strip().split(",") for line in f.readlines()]

steps1 = steps[0]
steps2 = steps[1]

coords1 = [(0,0)]
for step in steps1:
    last_coord = coords1[-1]
    if step[0] == "R":
        for j in range(1, int(step[1:])+1):
            coords1.append((last_coord[0]+j, last_coord[1]))
    elif step[0] == "L":
        for j in range(1, int(step[1:])+1):
            coords1.append((last_coord[0]-j, last_coord[1]))
    elif step[0] == "U":
        for j in range(1, int(step[1:])+1):
            coords1.append((last_coord[0], last_coord[1]+j))
    else:
        for j in range(1, int(step[1:])+1):
            coords1.append((last_coord[0], last_coord[1]-j))

coords2 = [(0,0)]
for step in steps2:
    last_coord = coords2[-1]
    if step[0] == "R":
        for j in range(1, int(step[1:])+1):
            coords2.append((last_coord[0]+j, last_coord[1]))
    elif step[0] == "L":
        for j in range(1, int(step[1:])+1):
            coords2.append((last_coord[0]-j, last_coord[1]))
    elif step[0] == "U":
        for j in range(1, int(step[1:])+1):
            coords2.append((last_coord[0], last_coord[1]+j))
    else:
        for j in range(1, int(step[1:])+1):
            coords2.append((last_coord[0], last_coord[1]-j))

intersections = list(set(coords1).intersection(coords2))
distances = [sum(map(abs, val)) for val in intersections]

print("Solution is {}".format(sorted(zip(distances, intersections), key=itemgetter(0))[1][0]))
