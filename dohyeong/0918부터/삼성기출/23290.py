# m : 물고기수 , s : 복제 횟수
m,s = map(int, input().split())
# 물고기 정보 넣기 위해 3차원배열 선언
graph = [[[] for _ in range(4)] for _ in range(4)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
# 방향 정보 -1해서 넣기 주의, 위치정보도 -1해서 넣기
for _ in range(m):
    f_x, f_y, f_dir = map(int, input().split())
    graph[f_x-1][f_y-1].append(f_dir-1)

s_x, s_y = map(int, input().split()) # 상어 위치
fish_smell = []
# 좌표와 방향이 주어졌을때, 물고기 이동시키는 함수
def move_fish(x,y,dir):
    for i in range(8):
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 상어, 범위 밖, 냄새 있는 곳으로는 못감
        if 0<=nx<4 and 0<=ny<4:
            if nx != s_x and ny != s_y:
                if (nx,ny) not in fish_smell:
                    graph[nx][ny].append(dir)
                    graph[x][y].remove(dir) # 이동후 삭제
                    break
        # 없으면 반시계 45 회전
        dir = (dir-1) % 8

def dfs(now_x, now_y, visited, tmp_fish, depth, graph):
    if depth == 3:
        # 그래프, 상어 위치, 물고기 냄새정보 리턴 -> 그래프 처리 어떻게??
        return
    visited[now_x][now_y] = True
    for i in range(4):
        nx = now_x + sx[i]
        ny = now_y + sy[i]
        if 0<=nx<4 and 0<=ny<4:
            if graph[nx][ny]:# 물고기가 있는 칸이면
                for _ in range(len(graph[nx][ny])):
                    tmp_dir = graph[nx][ny].pop() # 해당 물고기 삭제
                    tmp_fish.append((nx, ny, tmp_dir)) # 물고기 냄새 후보군
                depth += 1
                dfs(nx, ny, visited, tmp_fish)
                visited[nx][ny] = False
                tmp_fish.pop()
                depth -= 1




    # 방향도 최종에 넣어야함 우선순위


# 복제 마법 시전 -> 복제 리스트 넣기
copy_fish = [] # 좌표, 방향
for i in range(4):
    for j in range(4):
        if graph[i][j]:
            for f in graph[i][j]:#있으면
                copy_fish.append((i,j,f))
# print(copy_fish)

# 물고기 이동
for i in range(4):
    for j in  range(4):
        if graph[i][j]:
            for f in graph[i][j]:
                move_fish(i,j,f) # 그래프 정보가 바뀜

# 상어 이동
# 현재 상어 위치에서 시작해서 dfs로 최적의 경우 리턴
visited = [[False]*4 for _ in range(4)]
depth = 0
sx = [-1,1,0,0]
sy = [0,0,-1,1]
tmp_fish = []
# 들어갔다 나오면서 visited 다시 지우기
dfs(s_x, s_y, visited)