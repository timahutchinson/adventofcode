f = open("../../../data/2017/4/data.txt")
lines = readlines(f)
close(f)

count = 0
for line in lines
    line = split(line, " ")
    if length(line) == length(Set(line))
        count += 1
    end
end

println("Solution is $count")
