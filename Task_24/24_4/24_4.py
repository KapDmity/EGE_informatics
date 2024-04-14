# Максимальное количество идущих подряд символов,
# среди которых A встречается ровно 100 раз

f = open('24_2024.txt', 'r').read()
a = []
for i in range(len(f) - 1):
    if f[i] == 'T':
        a.append(i)
mx = 0
for i in range(len(a) - 100):
    l_n = a[i + 100] - a[i]
    mx = max(mx, l_n)
print(mx)