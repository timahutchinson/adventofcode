with open('data.txt', 'rb') as f:
    x = [map(int, row.strip().split('\t')) for row in f.readlines()]

print 'Solution is %d' % sum([(max(row) - min(row)) for row in x])
