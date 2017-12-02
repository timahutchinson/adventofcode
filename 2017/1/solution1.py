with open('./data.txt', 'rb') as f:
    captcha = f.read().strip()
captcha += captcha[0]

total = 0
for i, digit in enumerate(captcha):
    try:
        if digit == captcha[i+1]:
            total += int(digit)
    except IndexError:
        pass

print "Solution is %d" % total