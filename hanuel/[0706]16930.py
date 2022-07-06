from collections import deque
dx, dy = [1,-1,0,0], [0,0,1,-1]

# 입력
N, M, K = map(int, input().split())
MAP = [ list(input()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

# 초기세팅 
check = [ [float('inf')]*M for _ in range(N)]  #float('inf') : 양의 무한대
q = deque()
q.append((x1, y1))
check[x1][y1] = 0

# bfs
while q:
    x,y = q.popleft()
    for k in range (4):
        nx, ny = x + dx[k], y + dy[k]
        cnt = 1
        while cnt <= K and 0<=nx<N and 0<=ny<M and check[nx][ny]>check[x][y] and MAP[nx][ny] == ".":
            if check[nx][ny] == float('inf'):
                q.append((nx,ny))
                check[nx][ny] = check[x][y] + 1
            nx += dx[k]
            ny += dy[k]
            cnt += 1

# 출력
if check[x2][y2] == float('inf'):
    print(-1)
else:
    print(check[x2][y2])

'''
백준 2178번 처럼 check판을 갱신해가며 카운팅
다만, check를 양의 무한대로 초기화 함 (<-> 2178에서는 평소처럼 0으로 초기화)
'''
'''
while 에 달린 추가 조건
- 한번에 최대 K만큼 이동할 수 있음 -> cnt=1로 시작해서 cnt<=K 까지
- check[nx][ny] > check[x][y] (<-> 2178에서는 check[nx][ny]==0)
    여기서 이 조건을 충족하는 경우는 2가지
    1) check[nx][ny]가 float('inf')인 경우
       : 방문(갱신)된적이 없다는 뜻 -> q에 추가해주고, check 갱신
    2) check[nx][ny]가 전에 방문(갱신)된적이 있지만 check[x][y]보다 큰 경우
       : 방문(갱신)된적이 있다 -> pass (근데 여기 좀 헷갈려 ㅠ)
=> 똑같은 방향(nx+=dx[k]; ny+=dy[k]) 으로 최대 K번(cnt=1 cnt+=1 cnt<=K) 이동
'''
'''
너무.. 어려웠다.. 흑흑..
결국 시간 안에 못 풀어서
다른 분 풀이 보고 공부했다
'''
