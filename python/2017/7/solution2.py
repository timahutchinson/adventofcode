import re
import itertools

def calc_weight(program):
    if program in supports:
        return sum([calc_weight(prog2) for prog2 in supports[program]]) + weights[program]
    else:
        return weights[program]

weights = dict()
supports = dict()
supported_by = dict()
with open("../../../data/2017/7/data.txt", "rb") as f:
    lines = f.readlines()
    for line in lines:
        m = re.search('([a-z]+) \((\d+)\).*', line)
        weights[m.group(1)] = int(m.group(2))

        splitline = re.split(' -> ', re.sub(' \(\d+\)', '', line.strip()))
        if len(splitline) == 2:
            supports[splitline[0]] = splitline[1].split(', ')

            for program in splitline[1].split(', '):
                supported_by[program] = splitline[0]

program = 'xegshds' # base program from part 1
while True:
    weights_list = [(prog, calc_weight(prog)) for prog in supports[program]]
    grouped_pairs = [(a, list(b)) for a, b in itertools.groupby(sorted(weights_list, key=lambda x: x[-1]),
                                                                key=lambda x: x[-1])]
    #import pdb; pdb.set_trace()
    if len(grouped_pairs) == 2:
        program = [b for a, b in grouped_pairs if len(b) == 1][0][0][0]
    else:
        weights_list = [(prog, calc_weight(prog)) for prog in supports[supported_by[program]]]
        grouped_pairs = [(a, list(b)) for a, b in itertools.groupby(sorted(weights_list, key=lambda x: x[-1]),
                                                                    key=lambda x: x[-1])]
        if len(grouped_pairs[0][1]) > len(grouped_pairs[1][1]):
            sol = weights[grouped_pairs[1][1][0][0]] - (grouped_pairs[1][0] - grouped_pairs[0][0])
            print "Solution is %d" % sol
        else:
            sol = weights[grouped_pairs[0][1][0][0]] - (grouped_pairs[0][0] - grouped_pairs[1][0])
            print "Solution is %d" % sol
        break
