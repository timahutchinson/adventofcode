import re, collections, string

total = 0
regex = r'([a-z-]+)(\d+)\[(\w+)\]'
with open('input.txt') as f:
    for code, sector, checksum in re.findall(regex, f.read()):
        letters = ''.join(c for c in code if c in string.ascii_lowercase)
        tops = [(-n,c) for c,n in collections.Counter(letters).most_common()]
        ranked = ''.join(c for n,c in sorted(tops))
        if ranked.startswith(checksum):
            total += int(sector)

print "Total is %s" % total
