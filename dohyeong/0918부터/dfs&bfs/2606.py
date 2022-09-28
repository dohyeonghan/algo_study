n = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    data[a][b], data[b][a] = 1, 1
visited = [False] * (n+1)
res = -1
def dfs(x):
    visited[x] = True
    for i in range(len(data[x])):
        if not visited[i] and data[x][i] == 1:
            dfs(i)

dfs(1)
for i in visited:
    if i == True:
        res += 1
print(res)