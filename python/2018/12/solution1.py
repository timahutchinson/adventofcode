with open("../../../data/2018/12/data.txt") as f:
    lines = [line.strip() for line in f.readlines()]
notes = [line.split(" => ") for line in lines[2:]]
notes, repl = zip(*notes)
state = ".." + lines[0].replace("initial state: ", "")

print(repl)
