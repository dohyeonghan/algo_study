from collections import deque
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n+1)

q = deque()
q.append(x)
visited[x] = 0
# print(q)
# print(graph[x])
while q:
    x = q.popleft()
    for i in graph[x]:
        # 기존에 도달했었으면 그게 최소값이므로 굳이 갈 필요 없음
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)
check = False
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)