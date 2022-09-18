n = int(input())

graph = [list(input()) for _ in range(n)]

# print(graph)
# 교체는 상하좌우로 하면 다음줄에서 상은 이미 교체했고, 하도 이미 교체했기 때문에 우, 하만 체크하면 됨
# 상하좌우로 일단 다한다고 했을 경우 만들어보기
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(graph):
    res = 1
    for i in range(n):
        # 행부분 체크
        # 본인 체크
        cnt = 1
        for j in range(1,n):
            # 현재 값이 이전 값과 같을 때
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            # 현재 값이 이전 값과 다를 때
            else:
                cnt = 1
            # 다 체크 했으면 max 값 찾기
            res = max(res, cnt)
        # 열부분 체크
        cnt = 1
        for j in range(1,n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
    return res

res = 0
for x in range(n):
    for y in range(n):
        # 행 부분 교체
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
                temp = check(graph)
                res = max(res, temp)
                # 다시 원상복귀
                graph[x][y], graph[nx][ny] = graph[nx][ny], graph[x][y]
print(res)
