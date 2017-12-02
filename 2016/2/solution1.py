keypad =[[1,2,3],[4,5,6],[7,8,9]]
coords = [1,1]
code = ''
x = []

with open('input.txt', 'rb') as f:
    for row in f:
        x.append(row.strip('\n'))

for instr in x:
    for s in instr:
        if s == 'R':
            if coords[1] + 1 <= 2:
                coords[1] += 1
        elif s == 'L':
            if coords[1] - 1 >= 0:
                coords[1] -= 1
        elif s == 'U':
            if coords[0] - 1 >= 0:
                coords[0] -= 1
        elif s == 'D':
            if coords[0] + 1 <= 2:
                coords[0] += 1
    code += str(keypad[coords[0]][coords[1]])
    coords = [1,1]

print "The code is %s" % code

