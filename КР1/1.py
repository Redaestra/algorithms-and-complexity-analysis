arr = list(map(int, input().split()))

n = len(arr)
res = [10**9] * n

left = -10**9
right = 10**9

for i in range(n):
    j = n - 1 - i

    if arr[i] == 0:
        left = i
    res[i] = min(res[i], i - left)

    if arr[j] == 0:
        right = j
    res[j] = min(res[j], right - j)

print(res)