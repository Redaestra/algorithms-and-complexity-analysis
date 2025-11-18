def is_dialog(s):
    n = len(s)
    
    # dp[i] = True, если первые i символов образуют валидный диалог
    dp = [False] * (n + 1)
    dp[0] = True
    
    one_words = {"out", "output", "puton"}
    puton_words = {"in", "input", "one"}
    all_words = one_words | puton_words
    
    for i in range(n + 1):
        if not dp[i]:
            continue
        
        # Пробуем добавить каждое слово
        for word in all_words:
            if s[i:i+len(word)] == word:
                dp[i + len(word)] = True
    
    return dp[n]

n = int(input())
for _ in range(n):
    s = input().strip()
    print("YES" if is_dialog(s) else "NO")
