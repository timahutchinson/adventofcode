import re
import string

with open("../../../data/2018/5/data.txt") as f:
    x = f.read().strip()

repat = '|'.join([''.join(i) for i in zip(list(string.ascii_uppercase), list(string.ascii_lowercase))] + [''.join(i) for i in zip(list(string.ascii_lowercase), list(string.ascii_uppercase))])
pattern = re.compile(repat)
while True:
    if pattern.findall(x):
        x = pattern.sub('', x)
    else:
        print(len(x))
        break
