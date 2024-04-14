# Максимальное количество идущих подряд символов,
# среди которых комбинация AB встречается ровно 50 раз

f = open('24_13715.txt', 'r').read()
a = []
for i in range(len(f) - 1):
    if f[i] == 'A' and f[i + 1] == 'B':
        a.append(i)
print(a)
mx = 0
for i in range(len(a) - 51):
    l_n = (a[i + 51] - a[i])
    mx = max(mx, l_n)
print(mx)