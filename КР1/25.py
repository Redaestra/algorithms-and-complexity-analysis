# Проверяем, является ли массив неубывающей пирамидой (мин-кучей)
# Условие: для каждого i: a[i] <= a[2i+1] и a[i] <= a[2i+2], если такие потомки есть.

def is_min_heap(a):
    n = len(a)
    
    # Проходим по всем элементам, кроме листьев (но можно и по всем — без разницы)
    for i in range(n):
        left = 2 * i + 1     # индекс левого потомка
        right = 2 * i + 2    # индекс правого потомка

        # Проверяем левый потомок
        if left < n and a[i] > a[left]:
            return False
        # Проверяем правый потомок
        if right < n and a[i] > a[right]:
            return False

    return True


# === Основной ввод/вывод ===
n = int(input())
a = list(map(int, input().split()))

if is_min_heap(a):
    print("YES")
else:
    print("NO")
