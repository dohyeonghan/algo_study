from collections import deque

n,m=map(int,input().split())
miro=[]
for i in range (n):
    arr=list(map(int,input()))
    miro.append(arr)

#print(miro)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

count=1

def bfs(nx,ny):

    queue=deque()
    queue.append((nx,ny))

    while queue:
        x,y=queue.popleft()

        if x==n-1 and y==m-1:
            return miro[x][y]
        
        for i in range(4): #상하좌우로 모두 확인
            nx=x+dx[i]
            ny=y+dy[i]
            if nx==-1 or ny==-1 or nx==n or ny==m: #범위 넘어가면 무시하고 다른 방향 찾기
                continue
            if miro[nx][ny]==0: #못 가는 곳이면 무시하고 다른 방향찾기
                continue
            if miro[nx][ny]==1:
                miro[nx][ny]=miro[x][y]+1 #다음으로 넘어갈 곳의 값을 현재값+1해주기
                queue.append((nx,ny)) #큐에 현재 위치 다시 저장

result=bfs(0,0)
print(result)
