f = open('27-B_1.txt', 'r') # максимальная сумма, не кратная 5
n = int(f.readline())
a = 0
mn_dif = float('inf')
for i in f:
    x, y = map(int, i.split())
    a += max(x, y)
    dif = abs(x - y)
    if dif % 5 != 0 and dif != 0:
        mn_dif = min(mn_dif, dif)

if a % 5 != 0:
    print(a)
else:
    print(a - mn_dif)
