with open("../../../data/2019/1/data.txt") as f:
    masses = [int(line.strip()) for line in f.readlines()]

total_fuel = 0
for mass in masses:
    add_fuel = (mass // 3) - 2
    while add_fuel > 0:
        total_fuel += add_fuel
        add_fuel = (add_fuel // 3) - 2

print("Solution is {}".format(total_fuel))
