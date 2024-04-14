f = open('27990_B.txt', 'r')  # кол-во пар, где произведение элементов кратно 62
n = int(f.readline())
sm = 0
k_62 = 0
k_31 = 0
k_2 = 0
k_0 = 0
for i in f:
    a = int(i)
    if a % 62 == 0:
        k_62 += 1
    elif a % 31 == 0:
        k_31 += 1
    elif a % 2 == 0:
        k_2 += 1
    else:
        k_0 += 1
sm = k_2 * k_31 + k_2 * k_62 + k_31 * k_62
sm += k_62 * k_0
sm += k_62 * (k_62 - 1) // 2
print(sm)
