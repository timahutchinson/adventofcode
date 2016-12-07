import numpy as np

with open('input.csv', 'rb') as f:
    for row in f:
        x = row

x = x.split(', ')

loc = ['N',0,0]

for s in x:
    print loc
    print s
    if s[0] == 'R':
        if loc[0] == 'N':
            loc[0] = 'E'
            loc[1] += int(s[1:])
        elif loc[0] == 'E':
            loc[0] = 'S'
            loc[2] -= int(s[1:])
        elif loc[0] == 'S':
            loc[0] = 'W'
            loc[1] -= int(s[1:])
        elif loc[0] == 'W':
            loc[0] = 'N'
            loc[2] += int(s[1:])
    elif s[0] == 'L':
        if loc[0] == 'N':
            loc[0] = 'W'
            loc[1] -= int(s[1:])
	elif loc[0] == 'W':
            loc[0] = 'S'
            loc[2] -= int(s[1:])
	elif loc[0] == 'S':
            loc[0] = 'E'
            loc[1] += int(s[1:])
	elif loc[0] == 'E':
            loc[0] = 'N'
            loc[2] += int(s[1:])

print "Distance is %s" % (np.abs(loc[1]) + np.abs(loc[2]))
