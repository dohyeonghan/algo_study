n,m,x,y,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move_info = list(map(int, input().split()))
dice = [0,0,0,0,0,0]

def turn(now_dir):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if now_dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c

    elif now_dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d

    elif now_dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e

dx = [0,0,-1,1]
dy = [1,-1,0,0]
for di in move_info:
    # print('move:', di)
    nx = x + dx[di-1]
    ny = y + dy[di-1]
    if 0<=nx<n and 0<=ny<m:
        turn(di)
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[-1]
        else:
            dice[-1] = graph[nx][ny]
            graph[nx][ny] = 0
        x = nx
        y = ny
        print(dice[0])

