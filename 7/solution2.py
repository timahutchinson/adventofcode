import re

def check_aba(string):
    if string[1] == ' ':
        return False
    elif string[0] == string[1]:
        return False
    else:
        if string[0] == string[2]:
            return True

ips = []
with open('input.txt') as f:
    for line in f:
        ips.append(line.strip())

count = 0
for ip in ips:
    m = re.split(r'\[([^\]]+)\]', ip)
    parts = [' '.join(m[::2]), ' '.join(m[1::2])]
    for i in xrange(0,len(parts[0])-2):
        if check_aba(parts[0][i:i+3]):
            bab = parts[0][i+1] + parts[0][i] + parts[0][i+1]
            if bab in parts[1]:
                print parts[0][i:i+3]
                print bab
                print parts
                print '\n'
                count += 1
                break

print "Total is %s" % count
