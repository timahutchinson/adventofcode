with open("../../../data/2017/6/data.txt", "rb") as f:
    banks = [int(x.strip()) for x in f.read().split()]

configs = []
cycles = 0
nbanks = len(banks)
while True:
    cycles += 1
    ind = banks.index(max(banks))
    blocks = banks[ind]
    banks[ind] = 0
    for _ in range(blocks, 0, -1):
        ind += 1
        if ind == nbanks:
            ind = 0
        banks[ind] += 1
    if banks in configs:
        print "Solution is %d" % cycles
        break
    else:
        configs.append(banks[:])
