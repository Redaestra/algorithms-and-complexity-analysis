def count_pieces(wires, length):
    count = 0
    for wire in wires:
        count += wire // length
    return count

n, k = map(int, input().split())
wires = []
for _ in range(n):
    wires.append(int(input()))

left, right = 1, max(wires)
answer = 0

while left <= right:
    mid = (left + right) // 2
    pieces = count_pieces(wires, mid)
    
    if pieces >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
