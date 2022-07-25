def check(word):
    arr = []
    tmp = '?'
    for i in word:
        if tmp == i:
            continue
        else:
            if i in arr:
                return False
            tmp = i
            arr.append(i)
    return True
    
N = int(input())
ans = 0
for _ in range(N):
    word = input()
    if check(word)==True:
        ans += 1
print(ans)