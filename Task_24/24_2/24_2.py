# Максимальная последовательность вида KLMN,
# в начале и в конце последовательность может быть неполной

f = open('24_16388.txt', 'r').readline()
count = 1  # т.к. проверка идёт парами
mx = 0
a = f.replace('K', '1').replace('L', '2').replace('M', '3').replace('N', '4')
for i in range(len(a) - 1):
    if int(a[i + 1]) - int(a[i]) == 1:
        count += 1
    elif a[i + 1] == '1' and a[i] == '4':
        count += 1
    else:
        mx = max(mx, count)
        count = 1  # т.к. проверка идёт парами
print(mx)
