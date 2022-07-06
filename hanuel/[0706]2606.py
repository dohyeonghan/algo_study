from collections import deque

N = int(input())
K = int(input())
MAP = [ [0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    i,j = map(int, input().split())
    MAP[i][j] = 1
    MAP[j][i] = 1
check = [0]*(N+1)
ans = -1

q = deque()
q.append(1)
while q:
    x = q.popleft()
    if check[x] == 0:
        check[x] = 1
        ans+=1
        for i in range(1, N+1):
            if MAP[x][i] == 1 and check[i] == 0:
                q.append(i)
print(ans)
'''
백준 1260이랑 비슷 (정점, 간선)
'''