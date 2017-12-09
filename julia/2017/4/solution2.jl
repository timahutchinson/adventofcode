f = open("../../../data/2017/4/data.txt")
lines = readlines(f)
close(f)

count = 0
for line in lines
    invalid = false
    line = split(line, " ")
    for i = 1:length(line)
        for j = i+1:length(line)
            if Set(collect(line[i])) == Set(collect(line[j]))
                invalid = true
            end
        end
    end
    if !invalid
        count += 1
    end
end

println("Solution is $count")
