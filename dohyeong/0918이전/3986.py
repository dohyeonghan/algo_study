n = int(input())
words = [input() for _ in range(n)]
cnt = 0
for word in words:
    stack = []
    for i in range(len(word)):
        if stack and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])
    if not stack:
        cnt += 1
print(cnt)