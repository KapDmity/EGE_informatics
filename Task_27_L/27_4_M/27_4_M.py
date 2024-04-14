# Задача с наймом найбольшего количества рабочих
# Найм происходит парами, сумма баллов у пары рабочих должна быть > k

f = open('27A_13622.txt')
k = int(f.readline())
n = int(f.readline())
c = 0

a = []
for i in f:
    a.append(int(i))
a.sort()

st = 0
end = len(a) - 1
while st != end:
    if a[st] + a[end] > k:
        c += 2
        st += 1
        end -= 1
    else:
        st += 1
print(c)
