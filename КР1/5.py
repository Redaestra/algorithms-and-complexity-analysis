"""
Числа получаем как строки, преобразовывать в тип int нельзя из-за ограничения (можно использовать числа больше, чем поддерживает стандартный тип).

Для операций складываем или вычитаем соответствующие разряды чисел вручную, работая справа налево.

Для корректного сравнения, определения знака и работы с отрицательными числами реализуем обработку знака отдельно.

Результат выводим строкой.
"""



def remove_leading_zeros(s):
    """Удаляет ведущие нули и корректирует знак, если число отрицательное."""
    if s[0] == '-':
        s = '-' + s[1:].lstrip('0')
        if s == '-0':
            return '0'
        return s
    else:
        s = s.lstrip('0')
        return s if s else '0'

def compare_abs(a, b):
    """Сравнивает абсолютные значения строк a и b."""
    if len(a) != len(b):
        return len(a) - len(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])
    return 0

def add_abs(a, b):
    """Складывает два положительных числа в строковом виде."""
    result = []
    carry = 0
    a, b = a[::-1], b[::-1]
    maxlen = max(len(a), len(b))
    for i in range(maxlen):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        digit = digit_a + digit_b + carry
        carry = digit // 10
        result.append(str(digit % 10))
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])

def subtract_abs(a, b):
    """Вычитает два положительных числа в строковом виде, предполагая, что a >= b."""
    result = []
    a, b = a[::-1], b[::-1]
    borrow = 0
    for i in range(len(a)):
        digit_a = int(a[i])
        digit_b = int(b[i]) if i < len(b) else 0
        digit = digit_a - digit_b - borrow
        if digit < 0:
            digit += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(digit))
    # удаляем ведущие нули
    while len(result) > 1 and result[-1] == '0':
        result.pop()
    return ''.join(result[::-1])

def big_add_sub(a, op, b):
    # убираем ведущие нули
    a, b = remove_leading_zeros(a), remove_leading_zeros(b)

    # определяем знак каждого числа
    sign_a = -1 if a[0] == '-' else 1
    sign_b = -1 if b[0] == '-' else 1
    a = a[1:] if sign_a == -1 else a
    b = b[1:] if sign_b == -1 else b

    if op == '+':
        if sign_a == sign_b:
            result = add_abs(a, b)
            if sign_a == -1:
                result = '-' + result
        else:
            cmp = compare_abs(a, b)
            if cmp >= 0:
                result = subtract_abs(a, b)
                result = ('-' if sign_a == -1 else '') + result
            else:
                result = subtract_abs(b, a)
                result = ('-' if sign_b == -1 else '') + result
    elif op == '-':
        if sign_a != sign_b:
            result = add_abs(a, b)
            result = ('-' if sign_a == -1 else '') + result
        else:
            cmp = compare_abs(a, b)
            if cmp >= 0:
                result = subtract_abs(a, b)
                result = ('-' if sign_a == -1 else '') + result
            else:
                result = subtract_abs(b, a)
                result = ('-' if sign_a == 1 else '') + result
    else:
        raise ValueError("Некорректная операция")
    return remove_leading_zeros(result)

# Чтение входа
num1 = input().strip()
op = input().strip()
num2 = input().strip()
print(big_add_sub(num1, op, num2))
