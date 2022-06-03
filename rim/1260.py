from collections import deque


def dfs(graph,v,visited):
    visited[v]=1
    print(v,end=" ")
    # if len(graph[v])==0:
    #     return
    for i in graph[v]:
        if (visited[i]==0):
            dfs(graph,i,visited)


def bfs(graph,v,visited):
    queue=deque([v])

    visited[v]=1

    while queue:
        v=queue.popleft()
        print(v,end=" ")

        for i in graph[v]:
            if (visited[i]==0):
                queue.append(i)
                visited[i]=1


n,m,v=map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]

#print(graph)
for i in range(1,m+1):
    num1,num2=map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(1,n+1):
    graph[i].sort()

graphCopy=graph[:]
visitedCopy=[0 for i in range(n+1)]
    
dfs(graph,v,visited)
print()
bfs(graphCopy,v,visitedCopy)