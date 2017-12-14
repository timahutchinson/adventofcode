with open("../../../data/2017/10/data.txt", "rb") as f:
    steps = map(int, f.read().strip().split(','))

nums = range(256)
nnums = len(nums)
pos = 0
skip = 0

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

print "Solution is %d" % (nums[0] * nums[1])
