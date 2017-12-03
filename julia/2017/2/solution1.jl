f = open("../../../data/2017/2/data.txt")
lines = readlines(f)
close(f)

total = 0
for line in lines
    splitline = map(x->parse(Int,x), split(line, "\t"))
    total += maximum(splitline) - minimum(splitline)
end

println("Solution is $total")
