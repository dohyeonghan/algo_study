n = int(input()) # 맵
k = int(input()) # 사과
data = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    a,b = map(int, input().split())
    data[a][b] = 1 # 사과 있는 자리는 1
info = []
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

x,y = 1, 1
data[x][y] = 2
time = 0
direction = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
info_idx = 0
q = [(x,y)]

while True:
    nx, ny = x + dx[direction], y + dy[direction]
    if 1<=nx<=n and 1<=ny<=n and data[nx][ny] != 2:
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.pop(0)
            data[px][py] = 0
        if data[nx][ny] == 1:
            data[nx][ny] = 2
            q.append((nx,ny))
    else:
        time += 1
        break
    time += 1
    x,y = nx, ny
    # 시간 추가 후
    if info_idx < l and time == info[info_idx][0]:
        if info[info_idx][1] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        info_idx += 1
print(time)
