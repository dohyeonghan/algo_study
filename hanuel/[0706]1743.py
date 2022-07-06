from collections import deque

def BFS(i,j):
    q.append((i,j))
    check[i][j] = 1
    t=1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<N and 0<=ny<M and check[nx][ny]==0 and MAP[nx][ny]==1:
                check[nx][ny]=1
                t += 1
                q.append((nx,ny))
    return t
    
N, M, K = map(int, input().split())
MAP = [ [0]*M for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    MAP[i-1][j-1] = 1
check = [ [0]*M for _ in range(N)]

dx, dy = [1,-1,0,0], [0,0,1,-1]
q = deque()
ans = 0

for i in range(N):
    for j in range(M):
        if check[i][j] == 0 and MAP[i][j]==1:
            ans = max(ans, BFS(i,j))
print(ans)

'''
백준 1303이랑 비슷 (상하좌우탐색)
'''