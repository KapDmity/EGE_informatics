# № 1 Задача с заполнением грузовика товарами A и B
f = open("26.txt", "r")
n, m = map(int, f.readline().split())

b = []
for i in f:
    s = i.split()
    if s[-1] == "A":
        m -= int(s[0]) * int(s[1])
    else:
        b.append([int(s[0]), int(s[1]), int(s[0]) * int(s[1])])
b = sorted(b, key=lambda x: x[0])

count = 0
for i in b:
    if m - i[-1] >= 0:
        m -= i[-1]
        count += i[1]
    else:
        for j in range(i[1]):
            if m - i[0] >= 0:
                m -= i[0]
                count += 1
print(count, m)
