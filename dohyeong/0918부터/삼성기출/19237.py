n, m, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
graph = [[None]*n for _ in range(n)]
dir_data = list(map(int,input().split()))

p = [[[None]*4 for _ in range(4)] for _ in range(m)]
for i in range(m):#m마리의 상어중
    for j in range(4): #현재 방향별 우선순위
        tmp = list(map(int, input().split()))
        p[i][j] = tmp
# print(p)
print(graph)
print(data)
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            graph[i][j] = [0,0]
        else:
            dir = dir_data.pop(0)
            graph[i][j] = [data[i][j], dir-1]
dx = [-1,1,0,0]#상하좌우
dy = [0,0,-1,1]
smell_info = [[None]*n for _ in range(n)]

time = 0
while True:
    total = 0
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 0:
                total += len(graph[i][j])
    if total == 1:
        break
    if time > 1000:
        print(-1)
        break

    #자기자리에 냄새
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] != 0:
                smell_info[i][j] = [graph[i][j][0], k]

    # 상어 이동
    tmp_info = []
    move_info = []
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] != 0: #상어일떄
                tmp_d = p[graph[i][j][0]-1][graph[i][j][1]]
                check = False
                for k in range(4):
                    nx = i + dx[tmp_d[k]]
                    ny = j + dy[tmp_d[k]]
                    if len(smell_info[nx][ny]) < 1: # 냄새 없으면?
                        check = True
                        tmp_info.append([i,j], [nx,ny], k, graph[i][j][0])
                        candi = tmp_info[0]
                if check == False: # 냄새 없는게 없는 경우
                    for k in range(4):
                        nx = i + dx[tmp_d[k]]
                        ny = j + dy[tmp_d[k]]
                        if smell_info[nx][ny][0] == graph[i][j][0]: # 자기번호 있으면
                            tmp_info.append([i,j], [nx,ny], k, graph[i][j][0])
                    if len(tmp_info) > 0:
                        candi = tmp_info[0] # 우선순위대로 append
            move_info.append(candi)
    for m in move_info: # 실제 상어 이동
        graph[m[1][0]][m[1][1]] = [graph[i][j][0], k]
        graph[m[0][0]][m[0][1]] = [0,0]

    for i in range(n):
        for j in range(n):
            if smell_info[i][j][0] != 0:
                smell_info[i][j][1] -= 1
                if smell_info[i][j][1] == 0:
                    smell_info[i][j] = [0,0]

    # 상어 여러마리 있는지 체크
    for i in range(n):
        for j in range(n):
            if len(graph[i][j]) > 1:





