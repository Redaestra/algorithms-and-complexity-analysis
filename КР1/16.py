"""
Используем несколько свойств из математики:
1) Последовательность задана рекуррентно
2) В задаче каждый шаг находится остаток от деления на L, и из принципа Дирихле следует, что различных остатков от деления не более L, а значит они рано или поздно начнут повторяться (N подразумевает это)
3) Для всякой последовательности, содержащей циклы, актуально правило Флойда о черепахе и зайце: с его помощью, не храня весь массив целиком, мы можем узнать длину, а из неё начало цикла.
4) Зная это, достаточно посчитать количество полных вхождений цикла, и прибавить "хвосты" с обеих сторон.
"""


def f(x, M, L):
    return ((x * M) % (2**32 - 1)) % L



N, K, M, L = map(int, input().split())

# === Шаг 1: Находим длину цикла с помощью Флойда ===
tortoise = f(K, M, L)
hare = f(f(K, M, L), M, L)

# Поиск совпадения
while tortoise != hare:
    tortoise = f(tortoise, M, L)
    hare = f(f(hare, M, L), M, L)

# === Шаг 2: находим длину цикла ===
lam = 1
hare = f(tortoise, M, L)
while hare != tortoise:
    hare = f(hare, M, L)
    lam += 1

# === Шаг 3: находим начало цикла ===
mu = 0
tortoise = K
hare = K
for _ in range(lam):
    hare = f(hare, M, L)

while tortoise != hare:
    tortoise = f(tortoise, M, L)
    hare = f(hare, M, L)
    mu += 1

# === Шаг 4: генерируем элементы до конца цикла ===
seq = []
x = K
for _ in range(mu + lam):
    seq.append(x)
    x = f(x, M, L)

# === Шаг 5: считаем частоты (через list, без dict) ===
# L может быть большим, поэтому аккуратно
cnt = [0] * L
for i in range(min(N, mu)):
    cnt[seq[i]] += 1

if N > mu:
    remaining = N - mu
    full_cycles = remaining // lam
    tail = remaining % lam

    # Добавляем полный цикл
    for i in range(mu, mu + lam):
        cnt[seq[i]] += full_cycles

    # Добавляем остаток
    for i in range(mu, mu + tail):
        cnt[seq[i]] += 1

# === Шаг 6: вычисляем сумму нечётных элементов ===
total = 0
pos = 1
for val in range(L):
    c = cnt[val]
    if c == 0:
        continue
    # количество нечётных позиций внутри этого блока:
    odd_count = ((pos + c) // 2) - (pos // 2)
    total = (total + odd_count * val) % L
    pos += c

print(total % L)
