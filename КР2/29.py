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
