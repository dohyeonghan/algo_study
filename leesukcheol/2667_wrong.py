from collections import deque
def bfs(a,b,graph):
    
    
n = int(input())
matrix = [list(map(int,input())) for _ in range (n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []
for i in range (n):
    for j in range (n):
        if matrix[i][j]==1:
            cnt.append(bfs(i,j,matrix))
cnt.sort()
print(cnt)