k = int(input())
m = []
ans = 0
for i in range(4):
    row = []                    
    numbers = input()
    for j in range(4):           
        row.append(numbers[j])
    m.append(row)


c = [0] * 10

for i in range(4):
    for j in range(4):
        if m[i][j] != '.':
            c[int(m[i][j])] += 1

for el in c:
    if el <= k * 2 and el != 0:
        ans += 1

print(ans)