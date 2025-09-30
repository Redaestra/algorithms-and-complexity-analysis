def bubble_sort_animated(arr):
    print("=== Сортировка пузырьком ===")
    print(f"Начальный массив: {arr}\n")
    
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"--- Проход {i + 1} ---")
        
        for j in range(0, n - i - 1):
            print(f"  Сравниваем {arr[j]} и {arr[j+1]}", end=" → ")
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"МЕНЯЕМ → {arr}")
            else:
                print("не меняем")
        
        print(f"  Конец прохода {i + 1}: {arr}")
        
        if not swapped:
            print("  → Нет обменов, массив отсортирован досрочно!")
            break
        print()  # пустая строка для читаемости
    
    print(f"\n✅ Итог: {arr}")

def selection_sort_animated(arr):
    print("=== Сортировка выбором ===")
    print(f"Начальный массив: {arr}\n")
    
    n = len(arr)
    for i in range(n):
        min_idx = i
        print(f"--- Шаг {i + 1}: поиск минимума в [{i}:{n-1}] ---")
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                print(f"    Новый минимум: {arr[min_idx]} на позиции {min_idx}")
        
        # Обмен
        if min_idx != i:
            print(f"  Меняем {arr[i]} (поз. {i}) ↔ {arr[min_idx]} (поз. {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            print(f"  Минимум уже на месте ({arr[i]} на поз. {i})")
        
        print(f"  Массив после шага {i + 1}: {arr}\n")
    
    print(f"✅ Итог: {arr}")

def insertion_sort_animated(arr):
    print("=== Сортировка вставками ===")
    print(f"Начальный массив: {arr}\n")
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"--- Вставляем элемент {key} (поз. {i}) в отсортированную часть [{0}:{i-1}] ---")
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            print(f"  Сдвигаем {arr[j]} вправо → {arr}")
            j -= 1
        
        arr[j + 1] = key
        print(f"  Вставляем {key} на позицию {j + 1} → {arr}\n")
    
    print(f"✅ Итог: {arr}")

bubble_sort_animated([5, 1, 12, 59, 56, 12, 56])
print()
selection_sort_animated([5, 1, 12, 59, 56, 12, 56])
print()
insertion_sort_animated([5, 1, 12, 59, 56, 12, 56])