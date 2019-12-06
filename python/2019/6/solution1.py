from collections import defaultdict

with open("../../../data/2019/6/data.txt") as f:
    single_orbits = [a.strip().split(")") for a in f.readlines()]

sod = {a[1]:a[0] for a in single_orbits}
for val in sod.values():
    if val not in sod:
        sod[val] = 0
        break

orbits = defaultdict(list)
for key in sod:
    key2 = key
    while sod[key2]:
        orbits[key].append(sod[key2])
        key2 = sod[key2]

print("Solution is {}".format(sum([len(i) for i in orbits.values()])))
