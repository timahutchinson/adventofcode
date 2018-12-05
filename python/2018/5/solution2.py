import re
import string

with open("../../../data/2018/5/data.txt") as f:
    x = f.read().strip()

repat = '|'.join([''.join(i) for i in zip(list(string.ascii_uppercase), list(string.ascii_lowercase))] + [''.join(i) for i in zip(list(string.ascii_lowercase), list(string.ascii_uppercase))])
pattern = re.compile(repat)
lengths = []
for letter in string.ascii_uppercase:
    y = re.sub("%s|%s" % (letter, letter.lower()), "", x)
    while True:
        if pattern.findall(y):
            y = pattern.sub("", y)
        else:
            lengths.append(len(y))
            break

print(min(lengths))
