'''
총 Q번동안 과정 처리
할떄마다 L 달라짐 2**L씩 쪼개기

90도 회전

이후 전체 체크해서 네방향으로 얼음이 3개 미만이면 -1

Q번이 끝나면
전체 순회해서 얼음의 합

전체 dfs돌려서 제일 큰 덩어리 세기

'''
# graph = [[0] * 8 for _ in range(8)]
# cnt = 1
# for i in range(8):
#     for j in range(8):
#         graph[i][j] = cnt
#         cnt +=1
# L = 1
# step = 2**L
# start_arr = []
# for i in range(0,2**3,step):
#     for j in range(0,2**3,step):
#         # 부분 행렬 시작점 배열 만들기
#         start_arr.append((i,j))
#
# # for a in range(i,i+step):
#
# for i,j in start_arr:
#     res = [[0] * step for _ in range(step)]
#     for a in range(step):
#         for b in range(step):
#             res[b][step-a-1] = graph[a+i][b+j]
#     for a in range(i,i+step):
#         for b in range(j,j+step):
#             graph[a][b] = res[a-i][b-j]
# print(graph)
from collections import deque
n,q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**n)]
L = list(map(int, input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for l in range(q):
    if L[l] > 0:
        step = 2**L[l]
        start_arr = []
        for i in range(0,2**n,step):
            for j in range(0,2**n,step):
                start_arr.append((i,j))
        # 전체 부분 행렬 90도 회전
        for i,j in start_arr:
            res = [[0]*step for _ in range(step)]
            for a in range(step):
                for b in range(step):
                    res[b][step-a-1] = graph[a+i][b+j]
            for a in range(i,i+step):
                for b in range(j,j+step):
                    graph[a][b] = res[a-i][b-j]
    melt_list = []
    for i in range(2 ** n):
        for j in range(2 ** n):
            # 얼음 없을 때는 체크 안해도됨
            if graph[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < 2 ** n and 0 <= nj < 2 ** n:
                        if graph[ni][nj] > 0:
                            cnt += 1
                # 한방에 녹여야함 -> 처음에 순서대로 녹였다가 중복 적용됨
                if cnt < 3:
                    melt_list.append((i,j))
    for i, j in melt_list:
        graph[i][j] -= 1
# 얼음의 합
sum_ice = 0
for i in range(2**n):
    for j in range(2**n):
        sum_ice += graph[i][j]
print(sum_ice)
# 제일 큰 덩어리 체크
max_ice = -10e9
visited = [[False]*(2**n) for _ in range(2**n)]

def bfs(i,j):
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    ice_cnt = 1
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni<2**n and 0<=nj<2**n and not visited[ni][nj]:
                if graph[ni][nj] != 0:
                    visited[ni][nj] = True
                    q.append([ni,nj])
                    ice_cnt += 1
    return ice_cnt

for i in range(2**n):
    for j in range(2**n):
        if graph[i][j] > 0 and not visited[i][j]:
            ice_cnt = bfs(i,j)
            if ice_cnt > max_ice:
                max_ice = ice_cnt
if max_ice == -10e9:
    print(0)
else:
    print(max_ice)






