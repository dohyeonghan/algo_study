from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(color, x, y):

    q = deque()
    q.append((x,y))
    visited[x][y] = True
    block_size = 1
    rainbow = 0
    rainbow_xy = []
    block_xy = [[x,y]]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    block_xy.append([nx,ny])
                    block_size += 1
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    block_xy.append([nx, ny])
                    block_size += 1
                    rainbow += 1
                    rainbow_xy.append([nx,ny])
    # 무지개는 방문 상관없음
    for x,y in rainbow_xy:
        visited[x][y] = False
    return block_size, rainbow, block_xy

# 기준블록 찾기
def center(block_xy):
    tmp = []
    for x,y in block_xy:
        if graph[x][y] != 0:
            tmp.append((x,y))
    tmp.sort(key=lambda x:(x[0], x[1]))
    # print(tmp)
    return tmp[0][0], tmp[0][1]

def gravity(graph):
    for j in range(n):
        for i in range(n-2, -1, -1):
            if graph[i][j] > -1:
                now_x = i
                while True:
                    if now_x + 1 < n and graph[now_x + 1][j] == -2:
                        graph[now_x + 1][j] = graph[i][j]
                        graph[i][j] = -2
                        now_x += 1
                    else:
                        break


def rotate_90(graph):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-j-1][i] = graph[i][j]
    return res

# print(center([[2, 0], [2, 1], [2, 2]]))
# 오토 시뮬레이션 종료 조건 : 블록 그룹이 없을 때 -> 블록그룹이 None만 있을 때 종료
# check = False로 해놓고 다돌았는데 False면 break
res = 0
while True:
    value_list = []
    # 블록 그룹 확인
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            now_color = graph[i][j]# 현재 일반 컬러
            if graph[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                value = bfs(now_color, i,j) # 리턴 : 블록그룹개수, 무지개 개수, 좌표

            if value[0] > 1:
                center_xy = center(value[2])
                value_list.append([value[0], value[1], center_xy[0], center_xy[1], value[2]]) # 블록수, 무지개수, 기준 좌표 x,y, 전체 좌표

    if not value_list:
        break
    # 그룹 사이즈, 무지개 개수, 행, 열, 블록 좌표
    value_list.sort(reverse=True)
    now_group = value_list[0]
    # print(now_group)
    # 블록 그룹 제거
    for x,y in now_group[4]:
        graph[x][y] = -2
    # print(graph)
    res += now_group[0] ** 2
    # print(res)
    gravity(graph)

    graph = rotate_90(graph)

    gravity(graph)

print(res)
# print(max_block_group)
# print(res_xy)
