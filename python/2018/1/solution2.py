from collections import defaultdict
import itertools

with open("../../../data/2018/1/data.txt") as f:
    dfreqs = [int(line.strip()) for line in f.readlines()]

freqs = defaultdict(lambda: 0)
freq = 0
for dfreq in itertools.cycle(dfreqs):
    freq += dfreq
    if freqs[freq] == 1:
        print(freq)
        break
    else:
        freqs[freq] = 1
