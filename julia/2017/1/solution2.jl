f = open("../../../data/2017/1/data.txt")
captcha = readstring(f)
close(f)
captcha = replace(captcha ^ 2, "\n", "")

total = 0
n = Int(length(captcha) / 4)
for i = 1:(2*n-1)
    if captcha[i] == captcha[i+n]
        total += parse(Int, captcha[i])
    end
end

println("Solution is $total")
