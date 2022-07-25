def dfs_search(depth, total, add, sub, mul, div):
    global MAX, MIN
    if depth == N:
        MAX = max(total, MAX)
        MIN = min(total, MIN)
        return
    if add:
        dfs_search(depth+1, total+num[depth], add-1, sub, mul, div)
    if sub:
        dfs_search(depth+1, total-num[depth], add, sub-1, mul, div)
    if mul:
        dfs_search(depth+1, total*num[depth], add, sub, mul-1, div)
    if div:
        dfs_search(depth+1, int(total/num[depth]), add, sub, mul, div-1)
        
N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

MAX = -1e9
MIN = 1e9

dfs_search(1, num[0], add, sub, mul, div)
print(MAX)
print(MIN)

'''
백준 1260의 dfs
def DFS(v):
    print(str(v), end=" ")
    if v == M:
        return
    else:
        for i in range(1, N+1):
            if (MAP[v][i] == 1 and visited[i]==False):
                visited[i] = True
                DFS(i)
 
 
N, M, V = map(int, input().split())  
MAP = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
 
for i in range(M):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1
 
visited[V] = True
DFS(V)
'''