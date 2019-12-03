with open("../../../data/2019/2/data.txt") as f:
    ints = list(map(int, f.readlines()[0].split(",")))

ints[1] = 12
ints[2] = 2

ind = 0
while True:
    if ints[ind] == 1:
        ints[ints[ind+3]] = ints[ints[ind+1]] + ints[ints[ind+2]]
    elif ints[ind] == 2:
        ints[ints[ind+3]] = ints[ints[ind+1]] * ints[ints[ind+2]]
    elif ints[ind] == 99:
        break
    else:
        print("\nSomething went wrong!\n")
    ind += 4

print("Solution is {}".format(ints[0]))
