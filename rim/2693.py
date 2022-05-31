t=int(input())
for i in range(t):
    tempArr=list(map(int,input().split()))
    tempArr.sort()
    print(tempArr[-3])