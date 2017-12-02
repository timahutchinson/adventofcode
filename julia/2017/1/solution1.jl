f = open("../../../data/2017/1/data.txt")
captcha = readstring(f)
close(f)
captcha = replace(string(captcha, captcha[1]), "\n", "")

total = 0
for i = 1:length(captcha)-1
    if captcha[i] == captcha[i+1]
        total += parse(Int, captcha[i])
    end
end

println("Solution is $total")
