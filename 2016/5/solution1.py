import hashlib
from sys import stderr

doorid = 'ffykfhsq'

password = ''
index = 0
while len(password) < 8:
    stderr.write("\rFound: %s, hashing %s..." % (len(password),doorid+str(index)))
    m = hashlib.md5()
    m.update(doorid + '%s' % index)
    if m.hexdigest()[0:5] == '00000':
        password += m.hexdigest()[5]
    index += 1

print "\nPassword is %s" % password
