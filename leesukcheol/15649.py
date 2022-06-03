from itertools import permutations
n, m = list(map(int,input().split()))
arr = [i for i in range (1,n+1)]
for i in (permutations(arr,m)): #nPm
    for j in range (m):
        print(i[j], end=" ")
    print()