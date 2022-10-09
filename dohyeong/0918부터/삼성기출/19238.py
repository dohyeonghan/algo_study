from collections import deque
n,m,now_fuel = map(int, input().split())
# 자연수라고 했으니 n+1로 지정
# graph = [list(map(int, input().split())) for _ in range(n+1)] -> 인풋 문제 생김
graph = [[0] for _ in range(n+1)]
for i in range(1,n+1):
    graph[i].extend(list(map(int, input().split())))
# print(graph)
now_x, now_y = map(int, input().split())
# idx 0,1 : 출발지 좌표, idx 2,3 : 목적지 좌표
info = [list(map(int, input().split())) for _ in range(m)]

#나중에 행열 정렬을 위해
info.sort(key=lambda x: (x[0], x[1]))

# res = now_fuel
# 바닥나면 -1
# 모든 손님 이동 못할 경우 -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 거리정보만 내주는 bfs
def bfs(x,y):
    # 도달할 수 없으면 -1로
    dist = [[-1] * (n+1) for _ in range(n+1)]
    # 시작점은 도달할 수 있음
    dist[x][y] = 0
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<=nx<n+1 and 1<=ny<n+1:
                # 갈 수 없는 벽 체크, 이미 방문한곳 제외 -1인 방문 안한곳만
                if graph[nx][ny] != 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
    return dist

# 받은 거리정보로 손님 체크
def ready(dist):
    # 손님 좌표
    x,y = 0,0
    min_dist = 10e9
    for cust_info in info:
        # 손님에 해당하는 곳에 방문하지 않았을 경우
        if graph[cust_info[0]][cust_info[1]] != -1:
            if dist[cust_info[0]][cust_info[1]] < min_dist:
                min_dist = dist[cust_info[0]][cust_info[1]]
                x,y = cust_info[0], cust_info[1]

    if min_dist == 10e9: # 못태우러 가는경우
        return None
    else:
        return x, y, min_dist

cnt = len(info)
while True:
# 손님수 0이면 다 성공한것이므로 연료 리턴
    if cnt == 0:
        print(now_fuel)
        break
# 현재 위치에서 거리정보 받기 & 손님 최단거리 확인하기
    value = ready(bfs(now_x, now_y))
    # 거리정보가 -1 일때 못태우러감
    if value == None:
        print(-1)
        break
    else:
        # 연료 체크 : 태우러 이동중에 바닥나면 끝
        if now_fuel <= value[2]:
            print(now_fuel)
            break
        else: # 현재 연료와 택시 위치 체크, 손님도 없앰
            now_fuel -= value[2]
            now_x, now_y = value[0], value[1]
            graph[now_x][now_y] = -1

    # 목적지까지 거리
    price = bfs(now_x, now_y)
    # 손님 info에서 목적지 체크하기 -> 나중에 최적화
    for cust_info in info:
        if cust_info[0] == now_x and cust_info[1] == now_y:
            goal_x, goal_y = cust_info[2], cust_info[3]
    price_fuel = price[goal_x][goal_y]
    if price_fuel == -1:
        print(-1)
        break
    else:
        if now_fuel >= price_fuel:
            now_fuel += price_fuel
            # 이동했으면 현재 위치 초기화
            now_x, now_y = goal_x, goal_y
            # graph[now_x][now_y] = -1
            # 손님 처리 완료
            cnt -= 1

        else:
            print(-1)
            break


