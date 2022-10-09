'''
5 1 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0
'''
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# x, y 나무 있는 곳으로 체크한다는 가정하에
def grow(x,y, graph):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] != 0 and graph[nx][ny] != -1 and graph[nx][ny] != -2:
                cnt += 1
    graph[x][y] += cnt
# 성장
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != -1 and graph[i][j] != -2:
            grow(i,j, graph)
# print(graph)

def spread(x,y, graph, spread_info):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                cnt += 1
    spread_info.append([x,y,cnt])

# 번식은 순서대로 넣으면 중복 데이터 생겨버림
# 해결 : 좌표와 분배 점수 넣은 배열 만들어서 저장 후 한번에 돌리기
spread_info = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and graph[i][j] != -1 and graph[i][j] != -2:
            spread(i,j,graph, spread_info)
# print(spread_info)
temp = [[0] * n for _ in range(n)]
for x,y, cnt in spread_info:
    # print(x,y,cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                temp[nx][ny] += (graph[x][y] // cnt)
for x,y,cnt in spread_info:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = temp[nx][ny]

# print(graph)
# 제초제 뿌리는 것 체크

kill_info = []
ddx = [-2,-1,-1,-2,1,2,1,2]
ddy = [-2,-1,1,2,-1,-2,1,2]
for x,y,cnt in spread_info:
    tmp = graph[x][y]
    for i in range(8):
        nx = x + ddx[i]
        ny = y + ddy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] != 0 and graph[nx][ny] != -1 and graph[nx][ny] != -2:
                tmp += graph[nx][ny]
    kill_info.append([x,y,tmp])
kill_info.sort(key = lambda x: (x[2], x[0], x[1]))

# killinfo의 마지막 인자가 최대값
# print(kill_info[-1][2])

# 해골 표시

for i in range(8):
    nx = kill_info[-1][0] + ddx[i]
    ny = kill_info[-1][1] + ddy[i]
    if 0<=nx<n and 0<=ny<n:
        if graph[nx][ny] != 0 and graph[nx][ny] != -1 and graph[nx][ny] != -2:
            graph[nx][ny] = -2
print(graph)