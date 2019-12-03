def main():
    with open("../../../data/2019/2/data.txt") as f:
        orig_ints = list(map(int, f.readlines()[0].split(",")))

    for noun in range(100):
        for verb in range(100):
            ints = orig_ints[:]
            ints[1] = noun
            ints[2] = verb

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

            if ints[0] == 19690720:
                return 100 * noun + verb

print("Solution is {}".format(main()))
