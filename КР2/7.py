class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

ft = FenwickTree(n)
for i in range(1, n + 1):
    ft.update(i, arr[i])

for _ in range(m):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l, r = query[1], query[2]
        print(ft.range_sum(l, r))
    else:
        idx, val = query[1], query[2]
        delta = val - arr[idx]
        arr[idx] = val
        ft.update(idx, delta)
