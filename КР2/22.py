def unpack(s):
    stack = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            num = int(s[i])
            i += 2  # пропускаем цифру и '['
            depth = 1
            start = i
            while depth > 0:
                if s[i] == '[':
                    depth += 1
                elif s[i] == ']':
                    depth -= 1
                i += 1
            substr = unpack(s[start:i-1])
            stack.append(substr * num)
        else:
            stack.append(s[i])
            i += 1
    
    return ''.join(stack)

n = int(input())
strings = [unpack(input().strip()) for _ in range(n)]

candidate = min(strings, key=len)

while candidate:
    if all(s.startswith(candidate) for s in strings):
        break
    candidate = candidate[:-1]

print(candidate)
