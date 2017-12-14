import re

with open("../../../data/2017/10/data.txt", "rb") as f:
    steps = map(ord, list(f.read().strip())) + [17, 31, 73, 47, 23]

nums = range(256)
nnums = len(nums)
pos = 0
skip = 0

for _ in range(64):
    for step in steps:
        #import pdb; pdb.set_trace()
        if (pos + step) >= nnums:
            templist = nums[pos:] + nums[:step - (nnums - pos)]
            templist_r = list(reversed(templist))
            nums[pos:] = templist_r[:nnums - pos]
            nums[:step - (nnums - pos)] = templist_r[nnums - pos:]
        else:
            templist = nums[pos:pos + step]
            templist_r = list(reversed(templist))
            nums[pos:pos + step] = templist_r
        pos += (step + skip)
        if pos > nnums:
            pos = pos % nnums
        skip += 1

dense_hash = []
block_len = 16
last = 0
while last < nnums-1:
    this_hash = 0
    block = nums[last:last+block_len]
    for element in block:
        this_hash = this_hash ^ element
    dense_hash.append(this_hash)
    last += block_len

knothash = ''
for num in dense_hash:
    hexed = re.sub('0x', '', hex(num))
    if len(hexed) == 2:
        knothash += hexed
    else:
        knothash += '0' + hexed

print "Solution is %s" % knothash
