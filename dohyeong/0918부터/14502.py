n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# 울타리 3개 선택 후 집어넣을 임시 그래프
temp = [[0] * m for _ in range(n)]
# 벽 3개 설치
res = 0
def dfs(cnt):
    global res
    # 종료조건 : cnt 0이 될때
    if cnt == 0:
        # 그래프 복사해서 넣어줘야함
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        # 해당 그래프로 바이러스 전염 시작
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    # 전염
                    spread(i,j)

        # cnt = check()
        res = max(res, check())
        return
        # 전염후 안전구역 개수 체크


    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt -= 1
                dfs(cnt)
                graph[i][j] = 0
                cnt += 1
def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    return cnt
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def spread(x,y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread(nx,ny)

dfs(3)
print(res)