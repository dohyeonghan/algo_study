from itertools import combinations
n, m = list(map(int,input().split()))
arr = [i for i in range (1,n+1)]
for i in (combinations(arr,m)): #nCm
    for j in range (m):
        print(i[j], end=" ")
    print()