N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)]
dungchi = []

for i in range(N):
    cnt = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    print(cnt,end=' ')