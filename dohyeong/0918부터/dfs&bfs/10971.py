n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_value = 1e9
def dfs(start, now, cnt, total):
    global min_value, visited
    if cnt == n-1:
        if data[now][start] != 0:
            total += data[now][start]
            if total < min_value:
                min_value = total
                return

    for j in range(n):
        if not visited[j] and data[now][j] != 0:
            visited[j]=True
            dfs(start, j, cnt+1, total+data[now][j])
            visited[j]=False

for i in range(n):
    visited[i] = True
    dfs(i,i,0,0)
    visited[i] = False
print(min_value)

'''
실수
- max, min 실수
- 도달하지 못하는 경우 고려
- 마지막에도 도달하지 못하는 경우 고려
- 카운트 0부터 시작해서 n번 체크해야되는데 1부터 시작해서 잘못 체크
'''