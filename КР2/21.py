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
