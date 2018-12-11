import re

with open("../../../data/2018/9/data.txt") as f:
    p = re.compile("(\d+) players; last marble is worth (\d+) points")
    nelves, nmarbles = map(int, p.findall(f.read().strip())[0])

nelves, nmarbles = 13, 7999

imarb = 0
current = 0
played = [0]
elf = -1
scores = [0] * nelves
while imarb < nmarbles:
    imarb += 1
    elf += 1
    if elf >= nelves:
        elf -= nelves
    if imarb % 23 == 0:
        scores[elf] += imarb
        current -= 7
        while current >= len(played):
            current -= len(played)
        scores[elf] += played.pop(current)
    else:
        current += 2
        while current > len(played):
            current -= len(played)
        played.insert(current, imarb)
    #print(played)

print(max(scores))
