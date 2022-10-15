graph = [[] for _ in range(4)]
fish_data = [[] for _ in range(4)]
# print(graph)
for i in range(4):
    data = list(map(int, input().split()))
    # print(data)
    for j in range(4):
        a,b = data[2*j], data[2*j+1]
        graph[i].append([a,b-1])
# print(graph)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
from copy import deepcopy
def find_fish(graph, num):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == num:
                return [i,j]
    return None
def solve(graph, now_x, now_y, total):
    global res
    # 백트래킹 위해서 그래프 정보 카피
    nxt_graph = deepcopy(graph)
    # 상어 현재위치에서 먹기
    shark_dir = nxt_graph[now_x][now_y][1]
    total += nxt_graph[now_x][now_y][0]
    if res < total:
        res = total
    nxt_graph[now_x][now_y] = [-1,-1] # 번호와 좌표 모두 -1로 초기화해서 먹은 것 표시

    # 물고기 이동 -> 1번부터 시작
    # 물고기 번호 순으로 체크해서 좌표 정리해주기
    for i in range(1, 17):
        # i에 해당하는 좌표 찾기
        if find_fish(nxt_graph, i) == None:
            continue
        else:
            fish_x, fish_y = find_fish(nxt_graph,i)
            dir = nxt_graph[fish_x][fish_y][1]
            for j in range(8):
                nx = fish_x + dx[dir]
                ny = fish_y + dy[dir]
                if 0<=nx<4 and 0<= ny <4:
                    if not (nx == now_x and ny == now_y):
                        nxt_graph[fish_x][fish_y][1] = dir
                        nxt_graph[fish_x][fish_y], nxt_graph[nx][ny] = nxt_graph[nx][ny], nxt_graph[fish_x][fish_y]
                        break
                dir = (dir+1) % 8

            # nx, ny = fish_x + dx[nxt_graph[fish_x][fish_y][1]], fish_y + dy[nxt_graph[fish_x][fish_y][1]]
            # if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or [nx,ny] == [now_x, now_y]:
            #     dir = nxt_graph[fish_x][fish_y][1]
            #     for j in range(8):
            #         # 방향 왼쪽으로 한칸
            #         dir = (dir - 1) % 8
            #         nx, ny = fish_x + dx[dir], fish_y + dy[dir]
            #         if 0 <= nx < 4 and 0 <= ny < 4 and [nx,ny] != [now_x,now_y]:
            #             nxt_graph[fish_x][fish_y], nxt_graph[nx][ny] = nxt_graph[nx][ny], nxt_graph[fish_x][fish_y]
            #             nxt_graph[fish_x][fish_y][1] = dir
            #             break # 돌다가 됐으면 그만 돌아야지!!
            #     #     nxt_graph[fish_x][fish_y][1] = (nxt_graph[fish_x][fish_y][1] - 1) % 8
            #     #     nx, ny = fish_x + dx[nxt_graph[fish_x][fish_y][1]], fish_y + dy[nxt_graph[fish_x][fish_y][1]]
            #     #     if 0 <= nx < 4 and 0 <= ny < 4:
            #     #         nxt_graph[fish_x][fish_y], nxt_graph[nx][ny] = nxt_graph[nx][ny], nxt_graph[fish_x][fish_y]
            #     # # 8방향동안 못찾았으면 가만히
            # else:
            #     nxt_graph[fish_x][fish_y], nxt_graph[nx][ny] = nxt_graph[nx][ny], nxt_graph[fish_x][fish_y]



    # 상어 이동
    # 스텝은 세번 안에
    for step in range(1,4):
        nx, ny = now_x + dx[shark_dir] * step, now_y + dy[shark_dir] * step
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: # 상어 스텝이 중간부터 시작해서 좌표를 벗어날때
            break
        # elif nxt_graph[nx][ny][0] == -1:
        #     break
        if nxt_graph[nx][ny][0] != -1:
            solve(nxt_graph, nx,ny, total)
res = 0
solve(graph, 0,0,0)
print(res)
