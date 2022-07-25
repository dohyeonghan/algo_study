'''
BFS(너비우선탐색)
- 현재 나의 위치에서 가장 가까운 노드들을 모두 방문
- queue
-> 최단거리, 임의의 경로 => "depth(깊이)"

from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    check[v] = 1
    
    while q:
        x = q.popleft() # 현재위치 POP
        if check[x]==0:
            check[x]=1 # 방문한 곳 CHECK
            print(x, end=' ')
            for i in range(N):
                if MAP[x][i]==1 and check[i]==0:
                    q.append(i) # 방문할 곳 APPEND

'''
'''
DFS(깊이우선탐색)
- 현재 나의 위치에서 연결된 브랜치를 모두 방문 후 다음 브랜치로 넘어감
- 스택 or 재귀함수
-> 모든 노드를 방문하고자 할 떄, 이동할 때마다 가중치가 붙을 때, 이동 과정에 여러 제약이 있을 때 => "재귀적인. 백트래킹, 모든 경우"
(탐색 시간은 더 걸리지만, 가중치에 대한 변수를 지속해서 관리 가능)

def dfs(v):
    if check[v]==1:
        return
    check[v] = 1
    print(x, end=' ')
    for i in range(N):
        if check[i]==0:
            dfs(i)
'''
'''
ex. 우리나라에서 직통도로로 연결된 지역 중, 서울과 경기도 사이에 존재하는 경로를 찾고싶을 때
DFS : 전국의 모든 도로를 다 살펴봐야 할 수도 있다
BFS : 서울과 인접한 도로 먼저 탐색
'''