class HashTable:
    def __init__(self, size=100000):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return v
        
        return None

n = int(input())
ht = HashTable()

for _ in range(n):
    query = input().split()
    cmd = query[0]
    
    if cmd == "put":
        key, value = int(query[1]), int(query[2])
        ht.put(key, value)
    elif cmd == "get":
        key = int(query[1])
        result = ht.get(key)
        print(result)
    elif cmd == "delete":
        key = int(query[1])
        result = ht.delete(key)
        print(result)
