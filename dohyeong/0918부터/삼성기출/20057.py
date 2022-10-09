'''
N * N
(r,c)
A[r][c] : 모래양
한번에 한칸, 격자 가운데부터

이동 -> 모래 흩뿌림
흩뿌리는 것 좌표를 네방향에 대해서 룩업 테이블 만들어놓기

현재 위치 x,y
다음 위치(y) nx,ny에 대해서 info 정보 파악, 현재 방향에 따라 인덱스 설정

현재 위치가 1,1이면 끝

이동 구현

'''
info = [[[-2,0,2],[-1,0,7],[-1,-1,10],[-1,1,1],[0,-2,5],[2,0,2],[1,0,7],[1,-1,10],[1,1,1]],
        [[-1,-1,1],[-1,1,1],[0,-1,7],[0,-2,2],[0,1,7],[0,2,2],[1,-1,10],[1,1,10],[2,0,5]],
        [[-1,-1,1],[1,-1,1],[-1,0,7],[-2,0,2],[1,0,7],[2,0,2],[-1,1,10],[1,1,10],[0,2,5]],
        [[-2,0,5],[-1,-1,10],[-1,1,10],[0,-2,2],[0,-1,7],[0,1,7],[0,2,2],[1,-1,1],[1,1,1]]]


# 현재위치
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
now_x, now_y = n // 2, n // 2
# 두번 돌면 넘어가게끔
# 서, 남, 동, 북 순
dx = [0,1,0,-1]
dy = [-1,0,1,0]
visited = [[False] * n for _ in range(n)]
now_dir = -1
# 토네이도 방향 맞추기부터
outside = 0
visited[now_x][now_y] = True
while True:
    if now_x == 0 and now_y==0:
        break
    nd = (now_dir + 1) % 4
    nx = now_x + dx[nd]
    ny = now_y + dy[nd]
    if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
        visited[nx][ny] = True
        now_dir = nd
        # tornado(nx, ny, now_dir)
        now_x, now_y = nx,ny








#
# def sand(x,y, dir):
#     global dx, dy, res
#     # info[now_dir]를 순회하면서 해당 좌표에 해당 퍼센트만큼 모래를 현재 위치 모래를 이동
#     # 현재 위치 모래 : nx, ny의 모래 graph[nx][ny]
#     tmp_sand = 0
#     if graph[x][y] == 0:
#         return
#     for i in info[dir]:
#         nxt_x = x + i[0]
#         nxt_y = y + i[1]
#         if 0<=nxt_x<n and 0<=nxt_y<n:
#             graph[nxt_x][nxt_y] += (graph[x][y] * i[2]) // 100
#         else:
#             res += (graph[x][y] * i[2]) // 100
#
#         tmp_sand += (graph[x][y] * i[2]) // 100
#     alpha_x = x + dx[dir]
#     alpha_y = y + dy[dir]
#     if 0<=alpha_x<n and 0<=alpha_y<n:
#         graph[x+dx[dir]][y+dy[dir]] = graph[x][y] - tmp_sand
#     else:
#         res += graph[x][y] - tmp_sand
#     # 다돌렸으면 현재 위치 모래 제거
#     graph[x][y] = 0
#
# while True:
#     # print(now_x, now_y, now_dist, now_dir)
#     if now_x == 0 and now_y == 0:
#         break
#     # print(now_x, now_y, now_dir, now_dist)
#     nx = now_x + dx[now_dir]
#     ny = now_y + dy[now_dir]
#
#     sand(nx, ny, now_dir)
#     now_cnt += 1
#     # 이동했고 현재 카운트가 dist와 같으면 dist 타이밍 카운트에서 -1
#     if now_cnt == now_dist:
#         change_dist -= 1
#         now_dir = (now_dir + 1) % 4
#         now_cnt = 0
#         if change_dist == 0:
#             change_dist = 2
#             now_dist += 1
#     now_x, now_y = nx, ny
# #     print(now_x, now_y, now_dir, now_dist)
# # print(graph)
# # sum_sand = 0
# # for i in range(n):
# #     for j in range(n):
# #         sum_sand += graph[i][j]
# print(res)