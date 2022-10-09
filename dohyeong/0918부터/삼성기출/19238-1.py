from collections import deque
import math
import sys
import copy

sys.stdin = open("input.txt")

def Move(i, j, dir):
    if dir == 0 : return (i-1, j)
    elif dir == 1 : return (i, j-1)
    elif dir == 2: return (i, j+1)
    else : return (i+1, j)

def inBound(i, j):
    return 0 <= i < N+1 and 0 <= j < N+1

def findDest(si, sj, fuel, area, num): # 시작 좌표, 연료
    global gi
    global gj
    global gf
    visited = [[0] * (N+1) for _ in range(N+1)]
    q = deque()
    time = 0
    q.append((si, sj, fuel, time))
    visited[si][sj] = 1
    while q :
        i, j, f, time = q.popleft()
        if dest[num] == (i, j) : # 승객 찾으면
            gf =  f + time * 2
            gi = i
            gj = j
            return 0
        if f == 0 : # 연료 바닥남
            continue
        for dir in range(4):
            ni, nj = Move(i, j, dir)
            if not inBound(ni, nj) or area[ni][nj] == 1 or visited[ni][nj]: continue
            visited[ni][nj] = 1
            q.append((ni, nj, f - 1, time + 1))
    return -1

def BFS(si, sj, fuel, area): # 시작 좌표, 연료
    global cust
    visited = [[0] * (N+1) for _ in range(N+1)]
    q = deque()
    time = 0
    q.append((si, sj, fuel, time))
    visited[si][sj] = 1
    rider = []
    findT = math.inf
    while q :
        i, j, f, time = q.popleft()
        if time > findT : break
        if f == 0 : # 연료 바닥남
            return -1
        if cust[i][j] > 0 : # 승객 찾으면
            #if findDest(i, j, f, area, cust[i][j]) == -1 : return -1
            rider.append((i, j, cust[i][j], f))
            findT = time
            #cust[i][j] = 0
        else :
            for dir in range(4):
                ni, nj = Move(i, j, dir)
                if not inBound(ni, nj) or area[ni][nj] == 1 or visited[ni][nj]: continue
                visited[ni][nj] = 1
                q.append((ni, nj, f - 1, time + 1))
    if rider :
        rider.sort()
        i, j, num, f = rider[0]
        cust[i][j] = 0
        if findDest(i, j, f, area, num) == -1 : return -1


N, M, gf = map(int, input().split()) # 격자 크기, 승객 수, 초기 연료 양
area = [[1] * (N+1) for _ in range(N+1)]
cust = [[0] * (N+1) for _ in range(N+1)]
dest = dict()

for i in range(1, N+1):
    area[i] = list(map(int, input().split()))
    area[i].insert(0, 1)

gi, gj = map(int, input().split())

for i in range(1, M+1):
    ci, cj, di, dj = map(int, input().split())
    cust[ci][cj] = i
    dest[i] = (di, dj) # i 번 손님 목적지

for _ in range(M):
    if BFS(gi, gj, gf, area) == -1 :
        gf = -1
        break
for i in range(1, N+1):
    for j in range(1, N+1):
        if cust[i][j] : gf = -1
print(gf)