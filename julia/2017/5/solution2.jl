f = open("../../../data/2017/5/data.txt")
vals = map(x -> parse(Int,x), readlines(f))
close(f)

count = 0
ind = 1
while true
    old_val = vals[ind]
    if old_val >= 3
        vals[ind] -= 1
    else
        vals[ind] += 1
    end
    count += 1
    ind += old_val
    if ind > length(lines)
        println("Solution is $count")
        break
    end
end
