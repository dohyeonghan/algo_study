from collections import deque

def BFS(i,j):
    q.append((i,j))
    check[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<N and 0<=ny<M and check[nx][ny] == 0 and MAP[nx][ny]=='1':
                check[nx][ny] = check[x][y] + 1
                q.append((nx,ny))
            
N, M = map(int, input().split())
MAP = [ list(input()) for _ in range(N) ]
check = [ [0]*M for _ in range(N)]

dx,dy = [1,-1,0,0], [0,0,1,-1]
q = deque()

BFS(0,0)
print(check[-1][-1])

'''
백준 1303이랑 큰 틀은 비슷(상하좌우 탐색)하지만 세부적으로는 좀 다르다(check 쓰임새)
- check판에 오직 방문여부만 0,1로 표시
check[nx][ny] = 1
- check판을 갱신해가며 카운팅 
check[nx][ny] = check[x][y] + 1
'''