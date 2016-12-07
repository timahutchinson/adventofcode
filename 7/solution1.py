import re

def check_abba(string):
    if string[0] == string[1]:
        return False
    else:
        return True if string[:2] == string[3:1:-1] else False

ips = []
with open('input.txt') as f:
    for line in f:
        ips.append(line.strip())

count = 0
for ip in ips:
    p = True
    m = re.split(r'\[([^\]]+)\]', ip)
    parts = [' '.join(m[::2]), ' '.join(m[1::2])]
    for i in xrange(0,len(parts[0])-4):
        if check_abba(parts[0][i:i+4]):
            count += 1
            p = False
            for j in xrange(0,len(parts[1])-4):
                if check_abba(parts[1][j:j+4]):
                    count -= 1
                    break
            break
    if p: print	"%s\n" % ip

print "Total is %s" % count
