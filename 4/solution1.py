rooms = []

with open('input.txt', 'rb') as f:
    for line in f:
        rooms.append(line.strip())

total = 0
for room in rooms:
    #print room
    counts = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0,
              'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    for s in room[:-10]:
        if s != '-':
            counts[s] += 1
    #print counts
    #print room[-7:]
    if (counts[room[-6]] > counts[room[-5]]) or ( (counts[room[-6]] == counts[room[-5]]) and (room[-6] < room[-5]) ):
        if (counts[room[-5]] > counts[room[-4]]) or ( (counts[room[-5]] == counts[room[-4]]) and (room[-5] < room[-4]) ):
            if (counts[room[-4]] > counts[room[-3]]) or ( (counts[room[-4]] == counts[room[-3]]) and (room[-4] < room[-3]) ):
                if (counts[room[-3]] > counts[room[-2]]) or ( (counts[room[-3]] == counts[room[-2]]) and (room[-3] < room[-2]) ):
                    total += int(room[-10:-7])
                    #print 'YES\n\n\n'
                    print room[-10:-7]
    print '\n'

print "Total is: %s" % total
