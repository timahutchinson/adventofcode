with open('../../../data/2017/1/data.txt', 'rb') as f:
    captcha = f.read().strip()
captcha += captcha

total = 0
n = len(captcha) / 4
for i in xrange(2*n):
    if captcha[i] == captcha[i+n]:
            total += int(captcha[i])

print "Solution is %d" % total
