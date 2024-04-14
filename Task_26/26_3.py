with open('26_59821.txt', 'r') as file: # файл 26_3.txt для похожей задачи
    # n, k = map(int, file.readline().split())  # для похожей задачи с поиском номера детали по месту на ленте
    n = int(file.readline())
    a = []
    for i in range(n):
        x, y = map(int, file.readline().split())
        a.append([x, y, i + 1])

shl = []
pokr = []
for i in a:
    if i[0] <= i[1]:
        shl.append(i)
    else:
        pokr.append(i)

a.clear()
shl = sorted(shl, key=lambda x: x[0])
pokr = sorted(pokr, key=lambda x: x[1])

print(len(shl))  # количество деталей для шлифовки
print(len(pokr))  # количество деталей для покраски

if len(shl) > len(pokr):
    print(shl[-1][2])  # последняя деталь на конвейере
else:
    print(pokr[-1][2])  # последняя деталь на конвейере

konv = shl + pokr[::-1]
print(konv)
# print(konv[k - 1][2])  # номер детали по её месту на конвейере