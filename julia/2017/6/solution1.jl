f = open("../../../data/2017/6/data.txt")
banks = map(x -> parse(Int, x), split(readstring(f), "\t"))
close(f)

configs = []
cycles = 0
nbanks = length(banks)
while true
    cycles += 1
    ind = indmax(banks)
    blocks = banks[ind]
    banks[ind] = 0
    for _ = blocks:-1:1
        ind += 1
        if ind > nbanks
            ind = 1
        end
        banks[ind] += 1
    end
    if banks in configs
        println("Solution is $cycles")
        break
    else
        push!(configs, copy(banks))
    end
end
