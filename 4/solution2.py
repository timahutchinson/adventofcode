import re, collections, string

def caesar_cipher(s,n):
    s = s.replace('-', ' ')
    n = n % 26
    message = ''
    for letter in s:
        if letter == ' ':
            message += ' '
        else:
            shift = (ord(letter) - 97 + n) % 26
            message += str(unichr(shift + 97))
    return message

total = 0
regex = r'([a-z-]+)(\d+)\[(\w+)\]'
with open('input.txt') as f:
    for code, sector, checksum in re.findall(regex, f.read()):
        sector = int(sector)
        message = caesar_cipher(code, sector)
        if 'north' in message:
            print "North Pole sector is %s" % sector

