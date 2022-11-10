import copy
n, s = map(int, input().split())
data = list(map(int, input().split()))
# print(data)
cnt = 0
def dfs(now, total):
    global cnt
    if now == n:
        if total == s:
            cnt += 1
        return
    total1 = total
    total2 = total
    dfs(now + 1, total1 + data[now])
    dfs(now + 1, total2)
# 예외 -> 아무것도 안 골랐을경우 빼줘야함
dfs(0,0)

if s == 0:
    print(cnt-1)
else:
    print(cnt)