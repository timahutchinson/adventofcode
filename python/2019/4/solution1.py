def contains_double(d):
    s = str(d)
    if (s[0] == s[1]) | (s[1] == s[2]) | (s[2] == s[3]) | (s[3] == s[4]) | (s[4] == s[5]):
        return True
    else:
        return False


def doesnt_decrease(d):
    s = str(d)
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            return False
    return True


with open("../../../data/2019/4/data.txt") as f:
    low, high = f.readlines()[0].strip().split("-")
    
count = 0
for i in range(int(low), int(high)):
    if contains_double(i) & doesnt_decrease(i):
        count += 1

print(count)
