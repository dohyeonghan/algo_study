# graph = [[2,2,-1,3,1],[-2,-2,2,0,-1],[-2,-2,-2,1,2],[-1,-2,1,3,2],[-2,-2,2,2,1]]

# print(graph)
from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    visited[x][y] = True
    q = deque()
    q.append((x,y))
    block = [(x,y)]
    target = graph[x][y] # 타겟 숫자
    rainbow = []
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == target:
                    if graph[nx][ny] == 0:
                        rainbow.append((nx,ny))
                    else:
                        block.append((nx,ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
                else:
                    if graph[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        cnt += 1
                        rainbow.append((nx,ny))
                    elif graph[nx][ny] == target:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        cnt += 1
                        block.append((nx,ny))
                    else:
                        continue

    for r in rainbow: # 무지개는 다음 차례에서도 중복 가능
        visited[r[0]][r[1]] = False
    # print(rainbow)
    return [cnt, len(rainbow), block[0][0], block[0][1], block + rainbow]

def gravity(i,j):
    while True:
        ni = i + 1
        if ni < len(graph) and graph[ni][j] == -2: #이동 가능
            graph[ni][j] = graph[i][j]
            graph[i][j] = -2
            i = ni
        else:
            break

def rotate_90(graph):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-i-1] = graph[i][j]
    return res


res = 0 # 전체 점수
# 오토 플레이 while True -> 종료 조건 : 그룹 없을 때
check = False

while True:
    visited = [[False] * n for _ in range(n)] # 오토플레이 할때마다 초기화

    # test = bfs(1,0)
    # print(test)
    group_list = []
    # print(graph)
    for i in range(n):
        for j in range(n):
            # 일반 숫자일때 시작
            if graph[i][j] > 0 and not visited[i][j]:
                group = bfs(i, j)
                if group[0] > 1:
                    group_list.append(group)
        # if len(group_list) < 1:
        #     break
    group_list.sort(reverse=True)
    if len(group_list) < 1:
        break
    # print(group_list)
    max_group = group_list[0]
    # print(max_group)
    for m in max_group[4]:
        graph[m[0]][m[1]] = -2
    res += max_group[0] ** 2
                    # max_group[4] -> 전체 그룹 좌표
                    # for x,y in max_group:
                    #     graph[x][y] = -2 # 빈칸으로 초기화
                    # res += max_group[0] ** 2

        # 중력 적용
    for j in range(len(graph)):
        for i in range(len(graph)-1,-1,-1):
            # 빈칸 아니고, 검정 아닌것
            if graph[i][j] >= 0:
                gravity(i,j) # 그래프 변경

        # 반시계 방향으로 90도 : 시계 방향 270도
    for _ in range(3):
        tmp = rotate_90(graph)
        for i in range(n):
            for j in range(n):
                graph[i][j] = tmp[i][j]

    for j in range(len(graph)):
        for i in range(len(graph)-1,-1,-1):
            # 빈칸 아니고, 검정 아닌것
            if graph[i][j] >= 0:
                gravity(i,j) # 그래프 변경
print(res)