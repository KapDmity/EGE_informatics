# 9_EGKR
f = open('9_EGKR.txt', 'r')
count = 0
for i in f:
    a = list(map(int, i.split()))
    b = [a.count(j) for j in a]
    if b.count(2) == 6 and b.count(1) == 1:
        c = []
        ne_povt = 0
        for k in range(len(b)):
            if b[k] == 2:
                c.append(a[k])
            else:
                ne_povt = a[k]
        if (max(c) + min(c)) / 2 < ne_povt:
            count += 1
print(f'Result---{count}')
