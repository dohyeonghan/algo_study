from collections import deque

def bfs(i,j):
    q.append((i,j))
    check[i][j]=1
    t = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            while 0<=nx<N and 0<=ny<M and MAP[nx][ny]==1 and check[nx][ny]==0:
                q.append((nx,ny))
                check[nx][ny]=1
                t += 1
    return t        
        
N, M = map(int, input().split())
MAP = [ list(map(int,input().split())) for _ in range(N)]
check = [ [0]*M for _ in range(N)]
q = deque()

dx, dy = [1,-1,0,0], [0,0,1,-1]
cnt = 0
area = 0

for i in range (N):
    for j in range (M):
        if MAP[i][j]==1 and check[i][j]==0:
            cnt += 1
            area = max(area, bfs(i,j))
print(cnt)
print(area)