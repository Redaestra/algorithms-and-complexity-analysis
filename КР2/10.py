n = int(input())
seen = set()

for _ in range(n):
    word = input().strip()
    canonical = ''.join(sorted(word))
    seen.add(canonical)

print(len(seen))
