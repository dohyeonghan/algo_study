from collections import deque
n,m,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [1,2,3,4,5,6]

def turn_dice(dir):
    a,b,c,d,e,f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 0:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d,b,a,f,e,c
    elif dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c,b,f,a,e,d
    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b,f,c,d,a,e
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e,a,c,d,f,b

def bfs(x,y):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    cnt += 1
                    visited[nx][ny] =True
                    q.append((nx,ny))
    return cnt

def change_dir(a,b, dir):
    if a > b:
        if dir == 0:
            dir = 2
        elif dir == 1:
            dir = 3
        elif dir == 2:
            dir = 1
        else:
            dir = 0
    elif a < b:
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 0
        else:
            dir = 1
    else:
        return dir
    return dir

def reverse_dir(dir):
    if dir == 0:
        dir = 1
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 3
    else:
        dir = 2
    return dir


# 현재방향 동쪽(동서남북순)
dir = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x,y = 0,0
#n,m주의!!
res = 0
for _ in range(k):
    nx, ny = x + dx[dir], y + dy[dir]
    if 0<=nx<n and 0<=ny<m:
        turn_dice(dir)
        c = bfs(nx,ny)
        res += c * graph[nx][ny]
        x,y = nx, ny # 초기화 꼭
        # 이동방향 결정
        A,B = dice[-1],graph[x][y]
        dir = change_dir(A,B,dir)
    # 범위 밖이면 방향 반대로 한칸
    else:
        dir = reverse_dir(dir)
        nx, ny = x + dx[dir], y + dy[dir]
        turn_dice(dir)
        c = bfs(nx, ny)
        res += c * graph[nx][ny]
        x, y = nx, ny  # 초기화 꼭
        # 이동방향 결정
        A, B = dice[-1], graph[x][y]
        dir = change_dir(A, B, dir)
print(res)