import re
from operator import itemgetter

with open("../../../data/2017/12/data.txt", "rb") as f:
    x = [re.split(' <-> ', line.strip()) for line in f.readlines()]

x = {int(a):map(int, b.split(', ')) for a,b in x}
