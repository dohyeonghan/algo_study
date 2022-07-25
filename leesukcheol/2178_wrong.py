from collections import deque
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]= graph[x][y] + 1
                queue.append((nx,ny))        
    return graph[n-1][m-1]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range (n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bfs(0,0))

'''
1. dx, dy 선언하기
2. 시작점 프린트하며 함수 불러오기
3. queue 선언해서 처음 x좌표, y좌표 set로 묶어서 queue에 넣기
4. queue가 비는 경우는 끝에 닿는 경우밖에 없다. queue가 빌 때까지 반복문
5. x,y의 상하좌우를 다 비교하기. nx, ny로 선언.
6. (중요) 미로 벽(0)에 닿는 경우나, 미로 밖을 벗어나는 경우엔 continue 처리.
7. 1을 찾았으면 (이전 값 + 1)을 해주고 그 때의 x좌표(nx)와 y좌표(ny)를 queue에 삽입
'''