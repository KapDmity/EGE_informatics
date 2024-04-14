f = open('28129_B.txt', 'r')  # максимальная пара, где 1 или 2 числа кратны 7 и разный остатки от деления на 160
n = int(f.readline())
mx_7 = 0
res = []
for i in range(n):
    x = int(f.readline())
    if x % 7 == 0:
        mx_7 = max(mx_7, x)
    res += [x]
res.sort(reverse=True)
for i in res:
    if (mx_7 % 160) != (i % 160):
        print(mx_7, i)
    break
