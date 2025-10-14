    # Пирамидальная сортировка (heapsort)
# Без библиотек и встроенных функций, кроме len
# С реализацией кучи вручную и пользовательским сравнением

def compare(a, b):
    """
    Сравнение двух участников.
    Возвращает True, если a должен быть выше b по правилам:
    1) Больше решённых задач — выше
    2) При равенстве — меньше штраф — выше
    3) При равенстве — логин лексикографически меньше — выше
    """
    # Распаковываем
    login_a, solved_a, penalty_a = a
    login_b, solved_b, penalty_b = b

    # Больше решённых — выше
    if solved_a > solved_b:
        return True
    if solved_a < solved_b:
        return False

    # Меньше штраф — выше
    if penalty_a < penalty_b:
        return True
    if penalty_a > penalty_b:
        return False

    # Меньше логин — выше
    # Лексикографическое сравнение по символам вручную
    i = 0
    len_a = len(login_a)
    len_b = len(login_b)
    while i < len_a and i < len_b:
        if login_a[i] < login_b[i]:
            return True
        if login_a[i] > login_b[i]:
            return False
        i += 1
    # Если один логин префикс другого — короче = "меньше"
    return len_a < len_b


def sift_down(heap, i, n):
    """Просеивание вниз для кучи размера n"""
    while True:
        left = 2 * i + 1
        right = left + 1
        largest = i

        # Сравниваем с левым потомком
        if left < n and compare(heap[left], heap[largest]):
            largest = left

        # Сравниваем с правым потомком
        if right < n and compare(heap[right], heap[largest]):
            largest = right

        # Если текущий элемент больше обоих — стоп
        if largest == i:
            break

        # Иначе меняем местами
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        i = largest  # продолжаем просеивать вниз


def heapify(heap, n):
    """Построение кучи (просеивание всех родителей)"""
    i = n // 2 - 1
    while i >= 0:
        sift_down(heap, i, n)
        i -= 1


def heapsort(heap):
    """Пирамидальная сортировка"""
    n = len(heap)
    # Построить кучу
    heapify(heap, n)
    # Извлекать максимум и ставить в конец
    end = n - 1
    while end > 0:
        # Меняем местами корень и конец
        temp = heap[0]
        heap[0] = heap[end]
        heap[end] = temp
        # Просеиваем корень в куче уменьшенного размера
        sift_down(heap, 0, end)
        end -= 1


# === Основная программа ===
def main():
    n_str = input()
    n = int(n_str)
    arr = []

    i = 0
    while i < n:
        line = input().split()
        login = line[0]
        solved = int(line[1])
        penalty = int(line[2])
        arr.append((login, solved, penalty))
        i += 1

    # Сортировка кучей
    heapsort(arr)

    # После heapsort — массив отсортирован по возрастанию,
    # но нам нужен убывающий порядок (т.к. максимум — в начале)
    # значит, выводим в обратном порядке.
    i = n - 1
    while i >= 0:
        print(arr[i][0])
        i -= 1


# Запуск программы
main()
