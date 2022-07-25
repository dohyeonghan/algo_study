from collections import deque
m, n = map(int,input().split())
graph = [list(input().strip()) for _ in range (n)]
w, b = 0, 0
dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1] #상하좌우

def bfs(x,y,team): #i, j, graph[i][j]
    queue = deque()
    queue.append((x,y))
    cnt = 0
    graph[x][y] == 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x 