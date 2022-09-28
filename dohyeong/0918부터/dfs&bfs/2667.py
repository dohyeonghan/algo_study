n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))
# print(data)
visited = [[0] * n for _ in range(n)]
res = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global cnt
    global visited
    cnt += 1
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0 <=ny<n and not visited[nx][ny]:
            if data[nx][ny] == 1:
                dfs(nx,ny)
# print(data)
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i,j)
            res.append(cnt)

print(len(res))
for i in sorted(res):
    print(i)
# print(res)
# print(visited)