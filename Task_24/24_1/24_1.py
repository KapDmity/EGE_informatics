# Определите максимальное количество идущих подряд символов,
# среди которых символ F встречается 1 раз

f = open('24_1.txt', 'r').read()
a = f.split('F')

mx_l = 0
for i in range(len(a) - 1):
    mx_l = max(mx_l, len(a[i] + 'F' + a[i + 1]))

print(mx_l)
