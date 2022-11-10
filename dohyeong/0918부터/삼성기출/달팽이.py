n = 7
graph = [list(map(int, input().split())) for _ in range(n)]
# print(graph)
target = n ** 2 - 1
shark = ((n+1)//2-1, (n+1)//2-1)
'''
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 2 3 2 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3

11 12
21 22 
'''
# 좌 하 우 상 순으로 진행
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def tornado(graph):
    result = [0] # 상어부터 시작
    # print(result)
    now_x, now_y = shark
    # print(now_x, now_y)
    target = 0
    dist = 1
    flag = 0
    dir = 0
    check = False
    while True:
        for i in range(dist):
            nx = now_x + dx[dir]
            ny = now_y + dy[dir]
            # print(graph[nx][ny])
            target += 1
            if target == n**2:
                check = True
                break
            result.append(graph[nx][ny])
            now_x, now_y = nx, ny
        if check == True:
            break
        dir = (dir + 1) % 4
        flag += 1
        if flag == 2:
            flag = 0
            dist += 1
    return result
print(tornado(graph))
print(len(tornado(graph)))


