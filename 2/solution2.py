keypad =[ [' ', ' ', '1', ' ', ' '], [' ', '2', '3', '4', ' '],
          ['5', '6', '7', '8', '9'], [' ', 'A', 'B', 'C', ' '], [' ', ' ', 'D', ' ', ' '] ]
coords = [2,0]
code = ''
x = []

with open('input.txt', 'rb') as f:
    for row in f:
        x.append(row.strip('\n'))

for instr in x:
    for s in instr:
        print s
        print coords
        print keypad[coords[0]][coords[1]]
        if s == 'R':
            if coords[1] + 1 <= 4:
                if keypad[coords[0]][coords[1]+1] != ' ':
                    coords[1] += 1
        elif s == 'L':
            if coords[1] - 1 >= 0:
                if keypad[coords[0]][coords[1]-1] != ' ':
                    coords[1] -= 1
        elif s == 'U':
            if coords[0] - 1 >= 0:
                if keypad[coords[0]-1][coords[1]] != ' ':
                    coords[0] -= 1
        elif s == 'D':
            if coords[0] + 1 <= 4:
                if keypad[coords[0]+1][coords[1]] != ' ':
                    coords[0] += 1
    code += keypad[coords[0]][coords[1]]

print "The code is %s" % code

