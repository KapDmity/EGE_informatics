# 19 - 20 - 21
# +1 or *2

X = 49  # Предел камней перед выйгрышем
S = 8  # Кол-во камней в первой куче на старте


# 19
def f(s, t, h):
    if s + t > X and h == 1:
        return 0
    elif s + t > X and h == 2:
        return 1
    elif s + t <= X and h == 2:
        return 0
    if h % 2 == 0:
        return f(s + 1, t, h + 1) or f(s, t + 1, h + 1) or f(s * 2, t, h + 1) or f(s, t * 2, h + 1)
    else:
        return f(s + 1, t, h + 1) or f(s, t + 1, h + 1) or f(s * 2, t, h + 1) or f(s, t * 2, h + 1)


for t in range(1, X):
    if f(S, t, 0):
        print(f'№19---{t}')
        break


# 20
def f(s, t, h):
    if s + t > X and h == 1:
        return 0
    elif s + t > X and h == 2:
        return 0
    elif s + t > X and h == 3:
        return 1
    elif s + t <= X and h == 3:
        return 0
    if h % 2 == 0:
        return f(s + 1, t, h + 1) or f(s, t + 1, h + 1) or f(s * 2, t, h + 1) or f(s, t * 2, h + 1)
    else:
        return f(s + 1, t, h + 1) and f(s, t + 1, h + 1) and f(s * 2, t, h + 1) and f(s, t * 2, h + 1)


print('№20---', end='')
for t in range(1, X):
    if f(S, t, 0):
        print(t, end=' ')
print(end='\n')


# 21
def f(s, t, h):
    if s + t > X and h == 1:
        return 0
    elif s + t > X and h == 2:
        return 1
    elif s + t > X and h == 3:
        return 0
    elif s + t > X and h == 4:
        return 1
    elif s + t <= X and h == 4:
        return 0
    if h % 2 != 0:
        return f(s + 1, t, h + 1) or f(s, t + 1, h + 1) or f(s * 2, t, h + 1) or f(s, t * 2, h + 1)
    else:
        return f(s + 1, t, h + 1) and f(s, t + 1, h + 1) and f(s * 2, t, h + 1) and f(s, t * 2, h + 1)


def g(s, t, h):
    if s + t > X and h == 1:
        return 0
    elif s + t > X and h == 2:
        return 1
    elif s + t <= X and h == 2:
        return 0
    if h % 2 == 0:
        return g(s + 1, t, h + 1) and g(s, t + 1, h + 1) and g(s * 2, t, h + 1) and g(s, t * 2, h + 1)
    else:
        return g(s + 1, t, h + 1) or g(s, t + 1, h + 1) or g(s * 2, t, h + 1) or g(s, t * 2, h + 1)


for t in range(1, X):
    if f(S, t, 0) and not (g(S, t, 0)):
        print(f'№21---{t}')
