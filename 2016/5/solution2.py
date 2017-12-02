import hashlib
from sys import stderr

doorid = 'ffykfhsq'

password = ['','','','','','','','']
index = 0
found = 0
while found < 8:
    stderr.write("\rFound: %s, hashing %s..." % (found,doorid+str(index)))
    m = hashlib.md5()
    m.update(doorid + '%s' % index)
    if m.hexdigest()[0:5] == '00000':
        if m.hexdigest()[5] in ['0','1','2','3','4','5','6','7']:
            if password[int(m.hexdigest()[5])] == '':
                password[int(m.hexdigest()[5])] = m.hexdigest()[6]
                found += 1
    index += 1

print "\nPassword is %s" % ''.join(password)
