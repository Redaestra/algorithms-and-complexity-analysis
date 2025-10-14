"""
На каждом шаге бинарного поиска определяем, отсортирована ли левая или правая часть массива.

Если искомый элемент лежит в отсортированной части, продолжаем поиск там; иначе — в другой части.

Если элемент найден, возвращаем его индекс; если нет — возвращаем -1.
"""


def broken_search(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        # Левая половина отсортирована
        if arr[left] <= arr[mid]:
            if arr[left] <= k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Правая половина отсортирована
        else:
            if arr[mid] < k <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
print(broken_search(arr, k))
