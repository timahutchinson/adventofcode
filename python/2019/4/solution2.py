def contains_one_double(d):
    s = str(d)
    lens = []
    i = 0
    while i < len(s)-1:
        count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
            else:
                break
        lens.append(count)
        count = 1
        i = j
    return any([val == 2 for val in lens])


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
    if contains_one_double(i) & doesnt_decrease(i):
        count += 1
print(count)
