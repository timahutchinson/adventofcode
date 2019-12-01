with open("../../../data/2019/1/data.txt") as f:
    masses = [int(line.strip()) for line in f.readlines()]

print("Solution is {}".format(sum([(val // 3) - 2 for val in masses])))
