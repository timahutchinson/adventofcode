import re
from collections import defaultdict, deque

with open("../../../data/2018/9/data.txt") as f:
    p = re.compile("(\d+) players; last marble is worth (\d+) points")
    nelves, nmarbles = map(int, p.findall(f.read().strip())[0])

imarb = 0
played = deque([0])
scores = defaultdict(lambda: 0)
while imarb < nmarbles:
    imarb += 1
    if imarb % 23 == 0:
        scores[imarb % nelves] += imarb
        played.rotate(7)
        scores[imarb % nelves] += played.pop()
        played.rotate(-1)
    else:
        played.rotate(-1)
        played.append(imarb)

print(max(scores.values()))
