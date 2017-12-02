import numpy as np
import sys

with open('input.csv', 'rb') as f:
    for row in f:
        x = row

x = x.split(', ')

loc = ['N',0,0]
visited = [(0,0)]
solved = False

for s in x:
    if s[0] == 'R':
        if loc[0] == 'N':
            loc[0] = 'E'
            for i in xrange(loc[1]+1,loc[1]+int(s[1:])+1):
                if (i, loc[2]) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[2]))
                    sys.exit()
                else:
                    visited.append( (i,loc[2]) )
            loc[1] += int(s[1:])
        elif loc[0] == 'E':
            loc[0] = 'S'
            for i in xrange(loc[2]-1,loc[2]-int(s[1:])-1, -1):
                if (loc[1],i) in visited:
		    print "Distance is %s" % (np.abs(i) + np.abs(loc[1]))
                    sys.exit()
		else:
                    visited.append( (loc[1], i) )
            loc[2] -= int(s[1:])
        elif loc[0] == 'S':
            loc[0] = 'W'
            for i in xrange(loc[1]-1,loc[1]-int(s[1:])-1, -1):
                if (i, loc[2]) in visited:
		    print "Distance is %s" % (np.abs(i) + np.abs(loc[2]))
                    sys.exit()
		else:
                    visited.append( (i,loc[2]) )
            loc[1] -= int(s[1:])
        elif loc[0] == 'W':
            loc[0] = 'N'
            for i in xrange(loc[2]+1,loc[2]+int(s[1:])-1):
                if (loc[1],i) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[1]))
                    sys.exit()
                else:
                    visited.append( (loc[1], i) )
            loc[2] += int(s[1:])
    elif s[0] == 'L':
        if loc[0] == 'N':
            loc[0] = 'W'
            for i in xrange(loc[1]-1,loc[1]-int(s[1:])-1, -1):
                if (i, loc[2]) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[2]))
                    sys.exit()
                else:
                    visited.append( (i,loc[2]) )
            loc[1] -= int(s[1:])
	elif loc[0] == 'W':
            loc[0] = 'S'
            for i in xrange(loc[2]-1,loc[2]-int(s[1:])-1, -1):
                if (loc[1],i) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[1]))
                    sys.exit()
                else:
                    visited.append( (loc[1], i) )
            loc[2] -= int(s[1:])
	elif loc[0] == 'S':
            loc[0] = 'E'
            for i in xrange(loc[1]+1,loc[1]+int(s[1:])+1):
                if (i, loc[2]) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[2]))
                    sys.exit()
                else:
                    visited.append( (i,loc[1]) )
            loc[1] += int(s[1:])
	elif loc[0] == 'E':
            loc[0] = 'N'
            for i in xrange(loc[2]+1,loc[2]+int(s[1:])-1):
                if (loc[1],i) in visited:
                    print "Distance is %s" % (np.abs(i) + np.abs(loc[1]))
                    sys.exit()
                else:
                    visited.append( (loc[1], i) )
            loc[2] += int(s[1:])

if not solved: print "Didn't visit any location twice."
