"""
Реализуем вариант быстрой сортировки хоара (in-place, с двумя указателями) с кастомным компаратором cmp - функцией, которая сравнивает два списка по приоритетам.
"""


def quicksort(arr, left, right, cmp):
    if left >= right:
        return
    pivot = arr[(left + right) // 2]
    i, j = left, right
    while i <= j:
        while cmp(arr[i], pivot):  # если arr[i] "лучше" pivot
            i += 1
        while cmp(pivot, arr[j]):  # если pivot "лучше" arr[j]
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quicksort(arr, left, j, cmp)
    quicksort(arr, i, right, cmp)


def compare(rec1, rec2, priority):
    a1 = rec1[1]
    a2 = rec2[1]
    for p in priority:
        if a1[p - 1] != a2[p - 1]:
            return a1[p - 1] > a2[p - 1]  # невозрастание (от большего к меньшему)
    return False  # равны — порядок не меняем



# чтение входных данных
N = int(input())
k = int(input())
priority = list(map(int, input().split()))
records = []
for _ in range(N):
    parts = input().split()
    name = parts[0]
    nums = list(map(int, parts[1:]))
    records.append((name, nums))

# сортировка
quicksort(records, 0, len(records) - 1, lambda x, y: compare(x, y, priority))

# вывод результатов
for rec in records:
    print(rec[0])

