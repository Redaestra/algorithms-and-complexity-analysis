# Сборка решений задач на Python

## Задача 1 — Провода

**Условие.**
На складе есть провода различной целочисленной длины. Их можно разрезать на части. Необходимо получить K кусочков одинаковой целочисленной и как можно большей длины. Найти максимальную длину M, при которой можно получить по меньшей мере K кусочков этой длины. Все оставшиеся на складе куски проводов длиной меньшей M в подсчете не участвуют.

**Краткое объяснение решения.**
Используем бинарный поиск по ответу. Ключевая идея: если мы можем получить K кусочков длиной M, то мы можем получить K кусочков длиной L для любого L < M. То есть множество возможных ответов образует монотонный диапазон, что позволяет применить бинарный поиск. Для каждого кандидата M подсчитываем, сколько кусочков мы получим, если разрезать каждый провод на части длины M. Если получилось достаточно — ищем ещё большее значение, иначе ищем меньшее.

```python
def count_pieces(wires, length):
    count = 0
    for wire in wires:
        count += wire // length
    return count

n, k = map(int, input().split())
wires = []
for _ in range(n):
    wires.append(int(input()))

left, right = 1, max(wires)
answer = 0

while left <= right:
    mid = (left + right) // 2
    pieces = count_pieces(wires, mid)
    
    if pieces >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
```

**Пример.**
```
Ввод:
5 7
15
12
5
13
6

Вывод:
6
```


---

## Задача 2 — Ксерокопии

**Условие.**
Люда должна получить N копий одного документа, используя два ксерокса. Первый копирует лист за x секунд, второй — за y секунд. Можно использовать оба одновременно и копировать как с оригинала, так и с копии. Найти минимальное время.

**Краткое объяснение решения.**
Рассмотрим несколько стратегий: использовать только один ксерокс (время x·n или y·n), либо использовать оба одновременно. Если оба работают параллельно, то первый делает i копий за x·i, второй делает (n−i) копий за y·(n−i). Общее время — это max(x·i, y·(n−i)). Нам нужно найти i, при котором это максимум минимален. Оптимальное i находится примерно из условия x·i ≈ y·(n−i), откуда i ≈ y·n/(x+y). Проверяем несколько кандидатов в округе этого значения.

```python
def min_time(n, x, y):
    if n == 1:
        return min(x, y)
    
    if x > y:
        x, y = y, x
    
    # Один ксерокс делает все
    result = x * n
    
    # Оба работают параллельно
    # Первый делает i копий за x*i, второй делает (n-i) копий за y*(n-i)
    i = (y * n) // (x + y)
    
    for k in range(max(0, i - 1), min(n, i + 2)):
        time1 = x * k
        time2 = y * (n - k)
        result = min(result, max(time1, time2))
    
    return result

n, x, y = map(int, input().split())
print(min_time(n, x, y))
```

**Пример.**
```
Ввод:
4 1 1

Вывод:
3 (?)
```
Объяснение: Скопировать оригинал - 1 секунда. Ксерокс 1 копирует полученную копию, ксерокс 2 копирует оригинал (1 сек) параллельно. Итого 2 секунды, у авторов задачи же, ответ - 3.

---

## Задача 3 — Запросы сумм

**Условие.**
Дан массив V из N элементов. Нужно обрабатывать M запросов двух типов: (1) вычислить сумму элементов V[L]...V[R], (2) установить V[idx] = val. Элементы могут быть до 2³² − 1.

**Краткое объяснение решения.**
Используем структуру данных Fenwick Tree (Binary Indexed Tree). Она позволяет выполнять обновление и запрос префиксной суммы за O(log N). Идея основана на том, что каждое число можно представить как сумму степеней двойки (двоичное представление). Для дерева Fenwick храним блоки: tree[i] содержит сумму элементов на диапазоне, зависящем от того, сколько единиц в двоичном представлении i. При обновлении элемента добавляем дельту ко всем затронутым узлам. При запросе префиксной суммы суммируем соответствующие узлы. Для диапазонной суммы используем query(R) − query(L−1).

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ft = FenwickTree(n)
for i in range(1, n + 1):
    ft.update(i, arr[i])

for _ in range(m):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l, r = query[1], query[2]
        print(ft.range_sum(l, r))
    else:
        idx, val = query[1], query[2]
        delta = val - arr[idx]
        arr[idx] = val
        ft.update(idx, delta)
```

**Пример.**
```
Ввод:
10 8
1 7 15 8 9 15 15 19 5 19
1 1 8
1 6 8
1 0 6
2 6 6
2 1 6
2 0 9
1 4 7
1 3 6

Вывод:
93
39
70
49
38
```

---

## Задача 4 — Анаграммы

**Условие.**
Анаграммы — слова, составленные из одних и тех же букв в разном порядке (LOOP, POOL, POLO). На вход дано N слов одинаковой длины. Нужно определить количество различных комплектов анаграмм.

**Краткое объяснение решения.**
Для каждого слова найдём его "канонический" вид — отсортированную последовательность букв. Все анаграммы будут иметь одинаковый канонический вид. Поместим все канонические виды в множество (set), которое автоматически избавляет нас от дубликатов. Размер множества — это количество различных комплектов.

```python
n = int(input())
seen = set()

for _ in range(n):
    word = input().strip()
    canonical = ''.join(sorted(word))
    seen.add(canonical)

print(len(seen))
```

**Пример.**
```
Ввод:
8
BCB
ABA
BCB
BAA
BBC
CCB
CBC
CBC

Вывод:
3
```

---

## Задача 5 — Сопоставление по образцу

**Условие.**
Дано имя файла (только заглавные буквы) и образец с метасимволами. Символ `?` соответствует ровно одному символу, `*` — любому количеству символов (в том числе нулю). Проверить, соответствует ли имя образцу.

**Краткое объяснение решения.**
Используем динамическое программирование. dp[i][j] = True, если первые i символов имени соответствуют первым j символам образца. Базовый случай: dp[0][0] = True. Если образец начинается с нулей или звёзд, мы можем пропустить их в образце (звёзды могут соответствовать пустой строке). Переход: если символы совпадают или в образце стоит `?`, то dp[i][j] зависит от dp[i−1][j−1]. Если в образце стоит `*`, то она может соответствовать одному символу (dp[i−1][j]) или нулю (dp[i][j−1]).

```python
def matches(filename, pattern):
    n = len(filename)
    m = len(pattern)
    
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == '?' or filename[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[n][m]

filename = input().strip()
pattern = input().strip()

if matches(filename, pattern):
    print("YES")
else:
    print("NO")
```

**Пример.**
```
Ввод:
ABRACADABRA
ABRACA*BRA

Вывод:
YES
```

---

## Задача 6 — Хеш-таблица

**Условие.**
Реализовать хеш-таблицу с операциями: put (добавить/обновить), get (получить), delete (удалить). Нельзя использовать встроенные dict/HashMap. Разрешать коллизии методом цепочек.

**Краткое объяснение решения.**
Создаём массив "бакетов" (списков). Функция хеширования отображает ключ в индекс бакета (key % size). В каждом бакете хранятся пары (ключ, значение). При put: ищем ключ в бакете, если есть — обновляем, иначе добавляем. При get: ищем ключ в бакете, если есть — возвращаем значение, иначе None. При delete: удаляем пару из бакета и возвращаем её значение или None.

```python
class HashTable:
    def __init__(self, size=100000):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return v
        
        return None

n = int(input())
ht = HashTable()

for _ in range(n):
    query = input().split()
    cmd = query[0]
    
    if cmd == "put":
        key, value = int(query[1]), int(query[2])
        ht.put(key, value)
    elif cmd == "get":
        key = int(query[1])
        result = ht.get(key)
        print(result)
    elif cmd == "delete":
        key = int(query[1])
        result = ht.delete(key)
        print(result)
```

**Пример.**
```
Ввод:
8
get 9
put 9 1
get 9
put 9 2
get 9
put 9 3
get 9
delete 9

Вывод:
None
1
2
3
3
```

---

## Задача 7 — Привидение Ваня

**Условие.**
Ваня видит N плиток перед зеркалом. Часть плиток перед ним (видит оригинал и отражение), часть позади (видит только отражение). Нужно найти все возможные количества оригинальных плиток k, такие что первые k плиток совпадают с отражением плиток после позиции k.

**Краткое объяснение решения.**
Для каждого k от 0 до N проверяем: если первые k плиток совпадают с отражением последних k плиток (то есть последние k плиток в обратном порядке), то это валидное k. Используем хеширование для быстрого сравнения: вычисляем полиномиальный хеш для префикса и отражённого суффикса, сравниваем хеши.

```python
n, m = map(int, input().split())
tiles = list(map(int, input().split()))

MOD = 10**9 + 7
BASE = 31

results = []

for k in range(n + 1):
    left = tiles[:k]
    right = tiles[k:][::-1]
    
    if len(left) != len(right):
        continue
    
    hash_left = 0
    hash_right = 0
    
    for i in range(len(left)):
        hash_left = (hash_left * BASE + left[i]) % MOD
        hash_right = (hash_right * BASE + right[i]) % MOD
    
    if hash_left == hash_right:
        results.append(k)

for k in sorted(results, reverse=True):
    print(k, end=' ')
```

**Пример.**
```
Ввод:
5 0
1 2 3 2 1

Вывод:
5 2
```


---

## Задача 8 — Packed Prefix

**Условие.**
Даны строки в "запакованном виде": буквы — буквы, конкатенация строк — AB, повтор — n[A] означает "A повторена n раз". Найти длиннейший общий префикс распакованных строк.

**Краткое объяснение решения.**
Сначала распакуем каждую строку рекурсивно: при встрече с цифрой считываем число и подстроку в скобках, распаковываем подстроку и повторяем её n раз. Потом находим самую короткую распакованную строку (она может быть максимальным префиксом) и сокращаем её, пока она не станет префиксом всех остальных.

```python
def unpack(s):
    stack = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            num = int(s[i])
            i += 2  # пропускаем цифру и '['
            depth = 1
            start = i
            while depth > 0:
                if s[i] == '[':
                    depth += 1
                elif s[i] == ']':
                    depth -= 1
                i += 1
            substr = unpack(s[start:i-1])
            stack.append(substr * num)
        else:
            stack.append(s[i])
            i += 1
    
    return ''.join(stack)

n = int(input())
strings = [unpack(input().strip()) for _ in range(n)]

candidate = min(strings, key=len)

while candidate:
    if all(s.startswith(candidate) for s in strings):
        break
    candidate = candidate[:-1]

print(candidate)
```

**Пример.**
```
Ввод:
3
2[a]2[ab]
3[a]2[r2[t]]
a2[aa3[b]]

Вывод:
aaa
```

---

## Задача 9 — Странный диалог

**Условие.**
"One" может произносить слова: "out", "output", "puton". "Puton" может произносить: "in", "input", "one". Слова записываются подряд без пробелов. Диалог — это чередующиеся реплики, начинающиеся с кого-то и заканчивающиеся кем-то. Проверить, является ли строка диалогом.

**Краткое объяснение решения.**
Идея:
Используем массив dp размером N+1, где dp[i] означает: 'первые i символов строки можно разбить на допустимые слова'
Инициализируем dp[0] = True — пустая строка всегда разбивается корректно (нулевое количество слов)
Алгоритм:
Проходим по всем позициям i от 0 до N
Если dp[i] = True (то есть до позиции i строка разбивается), пробуем добавить каждое слово из словаря
Если слово совпадает с подстрокой от i до i+len(word), то dp[i + len(word)] = True
Это означает: если первые i символов разбиваются, и следующее слово допустимо, то первые i+len(word) символов тоже разбиваются

```python
def is_dialog(s):
    n = len(s)
    
    # dp[i] = True, если первые i символов образуют валидный диалог
    dp = [False] * (n + 1)
    dp[0] = True
    
    one_words = {"out", "output", "puton"}
    puton_words = {"in", "input", "one"}
    all_words = one_words | puton_words
    
    for i in range(n + 1):
        if not dp[i]:
            continue
        
        # Пробуем добавить каждое слово
        for word in all_words:
            if s[i:i+len(word)] == word:
                dp[i + len(word)] = True
    
    return dp[n]

n = int(input())
for _ in range(n):
    s = input().strip()
    print("YES" if is_dialog(s) else "NO")
```

**Пример.**
```
Ввод:
6
puton
inonputin
oneputonininputoutoutput
oneininputwooutoutput
outpu
utput

Вывод:
YES
NO
YES
NO
NO
NO
```

---

## Задача 10 — Шифр Бэкона

**Условие.**
Дана строка, состоящая только из строчных букв. Найти количество различных подстрок.

**Краткое объяснение решения.**
Для каждой длины подстроки от 1 до N используем rolling hash для вычисления хешей всех подстрок данной длины. Складываем все хеши в множество (которое автоматически избавляет от дубликатов). Размер множества — количество различных подстрок. Rolling hash позволяет избежать пересчёта хеша с нуля: для перемещения окна на один символ удаляем старый символ с левого конца и добавляем новый с правого.

```python
def count_distinct_substrings(s):
    n = len(s)
    hashes = set()
    
    MOD = 10**9 + 7
    BASE = 31
    
    # Для каждой длины подстроки
    for length in range(1, n + 1):
        pow_base = pow(BASE, length - 1, MOD)
        h = 0
        
        # Первый хеш
        for i in range(length):
            h = (h * BASE + ord(s[i])) % MOD
        hashes.add((length, h))
        
        # Rolling hash для остальных
        for i in range(length, n):
            h = (h - ord(s[i - length]) * pow_base) % MOD
            h = (h * BASE + ord(s[i])) % MOD
            hashes.add((length, h))
    
    return len(hashes)

s = input().strip()
print(count_distinct_substrings(s))
```

**Пример.**
```
Ввод:
aaba

Вывод:
8
```

