n,m,k = map(int, input().split())
balls = []
# balls = [list(map(int, input().split())) for _ in range(m)]
for _ in range(m):
    ri, ci, mi, si, di = list(map(int, input().split()))
    balls.append([ri-1, ci-1, mi, si, di])
graph = [[[] for _ in range(n)] for _ in range(n)]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,1,-1]

# 서로 다른 두 파이어볼이 같이 입력되는 경우는 없음 -> 처음에 고려안해도됨

# 파이어볼 이동
while balls:
    x, y, mi, si, di = balls.pop(0)
    nx = (x + dx[di] * si) % n
    ny = (y + dy[di] * si) % n
    graph[nx][ny].append([mi, si, di])

print(graph)

