# № 2
f = open("26(2).txt", "r")
n, m_1 = map(int, f.readline().split())
m = m_1

a = []
c = 0
for i in f:
    if 200 <= int(i) <= 210:
        m -= int(i)
        c += 1
    else:
        a.append(int(i))
a.sort()

i = 0
b = []
while (m - a[i]) >= 0:
    m -= a[i]
    c += 1
    i += 1
    b.append(a[i])

for k in range(len(b) - 1, -1, -1):
    m += b[k]
    for i in range(len(a) - 1, -1, -1):
        if m - a[i] >= 0:
            m -= a[i]
            break
print(c, m_1 - m)
