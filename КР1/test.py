n = int(input())
segments = []
i = 0
while i < n:
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    segments.append((a, b, i + 1))  # индекс 1-based
    i += 1

m = int(input())
queries = []
i = 0
while i < m:
    c = int(input())
    queries.append((c, i))  # сохраняем исходный индекс
    i += 1

# Ответы для каждой точки
answers = [-1] * m

# Стек активных отрезков: верхушка — минимальный вложенный
stack = []
seg_idx = 0

# Проходим по всем точкам-запросам
for point, q_idx in queries:
    # добавляем все новые отрезки, которые начинаются до точки
    while seg_idx < n and segments[seg_idx][0] <= point:
        a, b, idx = segments[seg_idx]
        # удаляем из стека только те отрезки, которые полностью включают новый
        while stack and stack[-1][0] <= a and stack[-1][1] >= b:
            stack.pop()
        stack.append((a, b, idx))
        seg_idx += 1

    # ищем минимальный отрезок, который включает точку
    while stack and not (stack[-1][0] <= point <= stack[-1][1]):
        stack.pop()

    if stack:
        answers[q_idx] = stack[-1][2]
    else:
        answers[q_idx] = -1

# Выводим ответы в порядке входных запросов
i = 0
while i < m:
    print(answers[i])
    i += 1