# Выбрать из последовательности три числа так,
# чтобы максимальное расстояние между числами было 2K,
# а сумма была максимально возможной

f = open('27-A.txt')
k = int(f.readline())
n = int(f.readline())
a = []
mx = 0
for i in f:
    a.append(int(i))

for i in range(len(a)):
    if i + 2 * k < len(a):
        x = a[i] + a[i + 2 * k]
        mx = max(mx, x)
    if mx == 126017:
        print(a[i], a[i + 2 * k])
        break

print(max(a))
print(mx + max(a))
