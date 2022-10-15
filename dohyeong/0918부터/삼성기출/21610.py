from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move_info = []
for _ in range(m):
    di, si = map(int, input().split())
    move_info.append((di-1, si))
# print(move_info)
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

# 비바라기 시전
cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for di, si in move_info:
    tmp = []
    for c in cloud:
        nx = (c[0] + dx[di] * si) % n
        ny = (c[1] + dy[di] * si) % n
        tmp.append((nx,ny))
    # print('tmp :', tmp)
    for t in tmp:
        graph[t[0]][t[1]] += 1
    # 구름 제거
    cloud = []
    # 물복사
    for t in tmp:
        cnt = 0
        for i in range(4):
            nx = t[0] + dx[2*i+1]
            ny = t[1] + dy[2*i+1]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] > 0:
                    cnt += 1
        graph[t[0]][t[1]] += cnt
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= 2:
                if (i,j) not in tmp:
                    cloud.append((i,j))
                    graph[i][j] -= 2
    # print(graph)
    # print(cloud)
res = 0
for i in range(n):
    for j in range(n):
       res += graph[i][j]
print(res)