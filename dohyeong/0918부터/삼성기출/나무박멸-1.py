n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

kill = [[0] * n for _ in range(n)]
kx = [-1, -1, 1, 1]
ky = [-1, 1, -1, 1]
res = 0


# 나무의 성장
def grow():
    # 한번에 처리하기 위해 해당 좌표와 추가되는 수 배열 선언
    grow_tmp = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        if graph[ni][nj] > 0:
                            cnt += 1
                grow_tmp.append((i, j, cnt))
    # 동시에 성장
    for i, j, cnt in grow_tmp:
        graph[i][j] += cnt


# print(grow(graph))

# 나무 번식
# def spread():
#     candi = []
#     for i in range(n):
#         for j in range(n):
#             # print('i,j:',(i,j))
#             if graph[i][j] > 0:  # 나무인지 확인
#                 tmp_spread = []
#                 cnt = 0
#                 for k in range(4):
#                     ni, nj = i + dx[k], j + dy[k]
#                     if 0 <= ni < n and 0 <= nj < n:
#                         if graph[ni][nj] == 0 and kill[ni][nj] == 0:  # 벽, 나무 없고 제초제 없을때
#                             # print('ni,nj:',(ni,nj))
#                             cnt += 1  # 번식이 가능한 칸수
#                             tmp_spread.append([ni, nj, 0])
#                 if cnt > 0:
#                     cnt = graph[i][j] // cnt
#                     # print(tmp_spread)
#                     for t in tmp_spread:
#                         t[2] = cnt
#                     for t in tmp_spread:
#                         candi.append(t)
#     # print(candi)
#     # 한번에 번식 시작
#     for i, j, cnt in candi:
#         graph[i][j] += cnt
def spread():
    add_tree = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                cnt = 0
                for l in range(4):
                    nx, ny = i + dx[l], j + dy[l]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 0 and kill[nx][ny] == 0:
                            cnt += 1
                for l in range(4):
                    nx, ny = i + dx[l], j + dy[l]
                    if 0 <= nx < n and 0 <= ny < n:
                        if graph[nx][ny] == 0 and kill[nx][ny] == 0:
                            add_tree[nx][ny] += graph[i][j] // cnt
    for i in range(n):
        for j in range(n):
            graph[i][j] += add_tree[i][j]


def find_kill():
    # 제초제는 나무 있는 곳에 뿌린다
    # 대각선 방향으로 k칸만큼 전파
    # 벽이 있거나 나무가 없으면 그칸까지는 전파 -> 나중에 전파에서 주의
    # 체크하는건 그냥 나무 개수만 체크
    global res
    max_kill = 0
    # max_x, max_y = 0,0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 0:
                tmp_kill = graph[i][j]
                for l in range(4):
                    ni, nj = i, j
                    for _ in range(k):
                        ni, nj = ni + kx[l], nj + ky[l]
                        if ni < 0 or ni >= n or nj < 0 or nj >= n:
                            break
                        if graph[ni][nj] <= 0:
                            break
                        tmp_kill += graph[ni][nj]
                        # if 0 <= ni < n and 0 <= nj < n:
                        #     if graph[ni][nj] == -1:
                        #         break
                        #     elif graph[ni][nj] > 0:
                        #         tmp_kill += graph[ni][nj]
                if max_kill < tmp_kill:
                    max_kill = tmp_kill
                    max_x, max_y = i, j
                    # print(tmp_kill)

    res += max_kill
    return max_x, max_y


def kill_tree(x, y):
    # 제초제 뿌리기
    # 현재 자리에 뿌려서 나무 0으로, 제초제 그래프 따로 만들어서 시간 체크
    # 나무 없거나 벽이어도 거기까지는 제초제 뿌리는 것 주의
    # kill 그래프

    if graph[x][y] > 0:
        kill[x][y] = c
        graph[x][y] = 0
        # print(x,y)

        for l in range(4):
            nx, ny = x, y
            for _ in range(k):
                nx, ny = nx + kx[l], nx + ky[l]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break
                if graph[nx][ny] < 0:
                    break
                if graph[nx][ny] == 0:
                    kill[nx][ny] = c
                    break
                graph[nx][ny] = 0
                kill[nx][ny] = c
        # for step in range(1, k + 1):
        #     for l in range(4):
        #         ni, nj = x + kx[l] * step, y + ky[l] * step
        #         if 0 <= ni < n and 0 <= nj < n:
        #             if graph[ni][nj] < 0:
        #                 break  # 벽이나 원래 나무 없으면 초기화는 kill만
        #             elif graph[ni][nj] == 0:
        #                 kill[ni][nj] = c
        #                 break
        #             else:
        #                 graph[ni][nj] = 0
        #                 kill[ni][nj] = c


def kill_down():
    for i in range(n):
        for j in range(n):
            if kill[i][j] > 0:
                kill[i][j] -= 1


# # main
# grow(graph)
# print(spread(graph))
# print(find_kill(graph))
# kill_x, kill_y = find_kill(graph)
# kill_down()
# print(kill_tree(kill_x, kill_y))
# # print(grow(graph))
# # print(spread(graph))
for _ in range(m):
    grow()
    spread()
    kill_down()
    x,y = find_kill()
    kill_tree(x,y)
print(res)

'''
5 2 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0


5 2 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0
'''