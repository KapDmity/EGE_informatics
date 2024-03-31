# 19 - 20 - 21
# +1 or *2

X = 25  # Предел камней перед выйгрышем


# 19
def f(s, h):
    if s > X and h == 1:
        return 0
    if s > X and h == 2:
        return 1
    if s <= X and h == 2:
        return 0
    if h % 2 == 0:  # ход Пети
        return f(s + 1, h + 1) or f(s * 2, h + 1)
    else:  # ход Вани
        return f(s + 1, h + 1) or f(s * 2, h + 1)


for s in range(1, X):
    if f(s, 0):
        print(f'№19---{s}')
        break


# 20
def f(s, h):
    if s > X and h == 1:
        return 0
    if s > X and h == 2:
        return 0
    if s > X and h == 3:
        return 1
    if s <= X and h == 3:
        return 0
    if h % 2 == 0:  # ход Пети
        return f(s + 1, h + 1) or f(s * 2, h + 1)
    else:  # ход Вани
        return f(s + 1, h + 1) and f(s * 2, h + 1)


print('№20---', end='')
for s in range(1, X):
    if f(s, 0):
        print(s, end=' ')
print(end='\n')


# 21
def g(s, h):
    if s > X and h == 1:
        return 0
    if s > X and h == 2:
        return 1
    if s <= X and h == 2:
        return 0
    if h % 2 == 0:  # ход Пети
        return g(s + 1, h + 1) and g(s * 2, h + 1)
    else:  # ход Вани
        return g(s + 1, h + 1) or g(s * 2, h + 1)


def f(s, h):
    if s > X and h == 1:
        return 0
    if s > X and h == 2:
        return 1
    if s > X and h == 3:
        return 0
    if s > X and h == 4:
        return 1
    if s <= X and h == 4:
        return 0
    if h % 2 == 0:  # ход Пети
        return f(s + 1, h + 1) and f(s * 2, h + 1)
    else:  # ход Вани
        return f(s + 1, h + 1) or f(s * 2, h + 1)


for s in range(1, X):
    if f(s, 0) and not (g(s, 0)):
        print(f'№21---{s}')
        break
