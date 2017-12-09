from collections import defaultdict
from functools import partial
from operator import itemgetter

def change_register(regs, regname, incdec, by):
    by = int(by)
    if incdec == 'inc':
        regs[regname] += by
    else:
        regs[regname] -= by
    return registers

with open("../../../data/2017/8/data.txt", "rb") as f:
    steps = [map(lambda x:x.split(' '), line.strip().split(' if ')) for line in f.readlines()]

registers = defaultdict(lambda: 0)
cr = partial(change_register, regs=registers)
max_seen = 0
for step in steps:
    change = step[0]
    cond = step[1]
    if cond[1] == '>':
        if registers[cond[0]] > int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    elif cond[1] == '<':
        if registers[cond[0]] < int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    elif cond[1] == '==':
        if registers[cond[0]] == int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    elif cond[1] == '>=':
        if registers[cond[0]] >= int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    elif cond[1] == '<=':
        if registers[cond[0]] <= int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    elif cond[1] == '!=':
        if registers[cond[0]] != int(cond[2]):
            registers = cr(regname=change[0], incdec=change[1], by=change[2])
    max_now = max(registers.items(), key=itemgetter(1))[1]
    if max_now > max_seen:
        max_seen = max_now

print "Solution is %d" % max_seen
