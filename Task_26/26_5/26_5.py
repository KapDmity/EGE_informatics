# Два окна для обслуживания клиентов
# Если услуга может быть оказана в любом окне, клиент выбирает то, где очередь меньше
# Если очереди в оба окна одинаковые, клиент выбирает окно с меньшим номером
# Если очередь в выбранное окно >= 14, то клиент уходит

f = open('26_13101.txt', 'r')
n = int(f.readline())
win_1_count = 0
win_2_count = 0
leaved = 0
win_1 = []
win_2 = []

a = []
for i in f:
    a.append(list(map(int, i.split())))
a.sort()

j = 0
break_flag = False
for minutes in range(1000):

    if a[j][0] == minutes:
        k = a[j]
        if a[j] == a[-1]:
            break_flag = True
        j += 1

        if k[2] == 1 and len(win_1) < 14:
            win_1.append(k)
            win_1_count += 1

        elif k[2] == 2 and len(win_2) < 14:
            win_2.append(k)
            win_2_count += 1

        elif k[2] == 0:
            if (len(win_2) < len(win_1)) and len(win_2) < 14:
                win_2.append(k)
                win_2_count += 1
            elif (len(win_2) >= len(win_1)) and len(win_1) < 14:
                win_1.append(k)
                win_1_count += 1
            else:
                leaved += 1
        else:
            leaved += 1

    if len(win_1) > 0:
        win_1[0][1] -= 1
        if win_1[0][1] == 0:
            win_1.pop(0)

    if len(win_2) > 0:
        win_2[0][1] -= 1
        if win_2[0][1] == 0:
            win_2.pop(0)

    if break_flag == True:
        break

print(win_1_count)
print(win_2_count)
print(leaved)
