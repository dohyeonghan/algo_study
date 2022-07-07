from collections import deque

def bfs(i,j):
    q.append((i,j))
    check[i][j]=1
    t=1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            while 0<=nx<N and 0<=ny<N and check[nx][ny]==0 and MAP[nx][ny]=='1':
                q.append((nx,ny))
                check[nx][ny]=1
                t+=1
    return t

N = int(input())
MAP = [list(input()) for _ in range(N)]
check = [ [0]*N for _ in range(N)]

dx,dy = [1,-1,0,0], [0,0,1,-1]
q = deque()
num = []
for i in range(N):
    for j in range(N):
        if MAP[i][j]=='1' and check[i][j]==0:
            num.append(bfs(i,j))
num.sort()
print(len(num))
for n in num:
    print(n)