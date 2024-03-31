# # Сортировка по второму элементу вложенных списков
# sorted_list = sorted(example_list, key=lambda x: x[1])


with open('k24-26-1.txt', 'r') as file:
    n = int(file.readline())
    a = []
    for i in file.readlines():
        x1, x2 = map(int, i.split())
        ls = [x1, x2, x1 + x2]
        a.append(ls)

a = sorted(a, key=lambda x: x[2])
# print(a)

d = [a[0]]

j = 0
for i in range(n - 1):
    if a[j][2] <= a[i + 1][0]:
        d.append(a[i + 1])
        j = i + 1
# print(d)
print(len(d))  # Результат_1

c = []
for i in range(n):
    if a[i][0] > d[-2][2]:
        c.append(a[i][0])
# print(c)
print(max(c) - d[-2][2])  # Результат_2
