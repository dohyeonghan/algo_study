from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i,j
            graph[i][j] = 0
now_size = 2
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    # visited = [[False] * n for _ in range(n)]
    tmp_graph = [[-1]*n for _ in range(n)] # -1인곳은 도달못하는곳 -> visited의 역할을 해준다
    q = deque()
    q.append((x,y))
    # visited[x][y] = True
    tmp_graph[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if now_size >= graph[nx][ny] and tmp_graph[nx][ny] == -1: # 현재 상어의 크기가 물고기보다 크거나 같아야 움질일 수 있다.
                    # visited[nx][ny] = True
                    q.append((nx,ny))
                    tmp_graph[nx][ny] = tmp_graph[x][y] + 1
    return tmp_graph
sizeup_flag = 0
res = 0
while True:
    fish_list = [] # 돌때마다 초기화

    dist_graph = bfs(now_x, now_y)
    for i in range(n):
        for j in range(n):
            if dist_graph[i][j] != -1:# 물고기면 -> 물고기인데도 도달이 불가능할 수 있구나
                if now_size > graph[i][j]:
                    if graph[i][j] != 0:#먹을 수 있다면
                        fish_list.append([dist_graph[i][j], i, j]) # 거리, 좌표 순으로 후보군 입력
    # 후보군 다 넣었으면
    # 있으면 정렬, 없으면 먹을 수 없는 상황이므로 종료
    if len(fish_list) < 1:
        break
    fish_list.sort() # 짧을수록, 좌표 작을수록이므로 그냥 sort해도됨
    # print(fish_list)
    # 제일 첫 물고기 제거, 상어 위치 옮기기
    eaten_fish = fish_list[0]
    res += eaten_fish[0] # 정답에 거리정보 합
    x,y = eaten_fish[1], eaten_fish[2]
    # 해당 좌표에 있는 물고기 제거, 상어 위치 옮기기
    graph[x][y] = 0
    now_x, now_y = x,y
    # 먹었으니 먹은 횟수 추가
    sizeup_flag += 1
    if sizeup_flag == now_size:
        now_size += 1
        sizeup_flag = 0
print(res)