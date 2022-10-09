# 전체 데이터

# 아기상어 현재 크기, 위치 변수

# 아기상어 시작 위치

# bfs : 모든 위치까지 최단 거리만 계산
# 최단거리 테이블 반환

# 최단거리 테이블 있을 때 먹을 물고기 찾기

# while 반복 : 먹을 물고기 찾고, 물고기 있으면 체크 없으면 끝

from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            array[now_x][now_y] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미
    dist = [[-1] * n for _ in range(n)]
    # 시작점은 도달가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                # 자신의 크기보다 작거나 같은 경우 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

# 최단거리 테이블이 주어졌을 때 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= array[i][j] < now_size:
                # 가장 가까운 물고기 한마리만 선택
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    # 먹을 수 있는 물고기가 없는 경우 == 최단 거리가 없는 경우
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist
result = 0
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 아무것도 없게 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0
