def make_alpha_dict():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    a_dict = {}
    for	letter in alpha:
        a_dict[letter] = 0
    return a_dict

ms = []

with open('input.txt', 'rb') as f:
    for line in f:
        ms.append(line.strip())

message = ''

for i in xrange(len(ms[0])):
    a_dict = make_alpha_dict()
    for m in ms:
        a_dict[m[i]] += 1
    message += max(a_dict, key=a_dict.get)

print "The message is %s" % message


