# Задача на временные интервалы
# Даны время начала и окончания каждого мероприятия

f = open('26_4.txt', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(list(map(int, f.readline().split())))

a.sort(key=lambda x: x[1])
fin = 0
count = []
for i in a:
    if fin <= i[0]:
        count.append(i)
        fin = i[1]
print(len(count))
print(count)

mx = 0
for i in range(len(a)- 1, 0, -1):
    if a[i][0] >= count[-2][1]:
        mx = max(mx, a[i][1])
print(mx)