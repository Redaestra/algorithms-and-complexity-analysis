def min_time(n, x, y):
    if n == 1:
        return min(x, y)
    
    if x > y:
        x, y = y, x
    
    # Один ксерокс делает все
    result = x * n
    
    # Оба работают параллельно
    # Первый делает i копий за x*i, второй делает (n-i) копий за y*(n-i)
    # Нужно найти i такое, что x*i = y*(n-i) (или близко к этому)
    
    # x*i = y*(n-i)
    # x*i = y*n - y*i
    # x*i + y*i = y*n
    # i*(x+y) = y*n
    # i = y*n / (x+y)
    
    i = (y * n) // (x + y)
    
    for k in range(max(0, i - 1), min(n, i + 2)):
        time1 = x * k
        time2 = y * (n - k)
        result = min(result, max(time1, time2))
    
    return result

n, x, y = map(int, input().split())
print(min_time(n, x, y))
