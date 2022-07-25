'''
deque : 양방향 큐 (앞, 뒤 양쪽 방향에서 엘리먼트를 추가하거나 제거 가능))
from collections import deque
deque.append(a) <- 오른쪽 끝에 삽입
deque.appendleft(a) <- 왼쪽 끝에 삽입
deque.pop() <- 오른쪽 끝 엘리먼트 반환 및 삭제
deque.popleft() <- 왼쪽 끝 엘리먼트 반환 및 삭제
deque.remove(a) <- a를 데크에서 찾아 삭제
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가
deque.rotate(num): 데크를 num만큼 회전
'''

# 백준 1260 bfs
from collections import deque
def BFS(v):
    Q = deque([])
    Q.append(v)
 
    while Q:
        x = Q.popleft()
        if check_BFS[x] is False:
            check_BFS[x] = True
            print(x, end=" ")
            for i in range(1, N+1):
                if MAP[x][i] == 1 and check_BFS[i] is False:
                    Q.append(i)
 
N, M, V = map(int, input().split())  # 정점, 간선, 탐색 시작 vertex
MAP = [[0] * (N+1) for _ in range(N+1)]
check_BFS = [False] * (N+1)
for i in range(M):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1
BFS(V)


# 백준 1303 bfs
from collections import deque
 
def BFS():
    q.append((i, j))
    check[i][j] = 1
    t = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] == MAP[x][y] and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))
                t += 1
    return t
 
# N: 가로 M : 세로
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
check = [[0] * N for _ in range(M)]
 
dx,dy=[1,-1,0,0],[0,0,1,-1]
q = deque()
B, W = 0, 0
 
for i in range(M):
    for j in range(N):
        if check[i][j] == 0:
            ans = BFS()
            if MAP[i][j] == 'W': W += ans ** 2
            else: B += ans ** 2
 
print(W, B)

'''
bfs 구현 순서
q = deque()
q.append(처음거)
check[처음거]=1
while q:
    x = q.popleft()
    if check[x]==0 (+추가적인 조건):
        check[x]=1
        q.append(x)
'''