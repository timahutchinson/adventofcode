using Combinatorics

f = open("../../../data/2017/2/data.txt")
lines = readlines(f)
close(f)

total = 0
for line in lines
    splitline = map(x->parse(Int,x), split(line, "\t"))
    for pair in combinations(splitline, 2)
        if maximum(pair) % minimum(pair) == 0
            total += maximum(pair) / minimum(pair)
        end
    end
end

println("Solution is $total")
