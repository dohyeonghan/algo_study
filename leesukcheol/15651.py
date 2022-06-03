from itertools import product
n, m = list(map(int, input().split()))
arr = [i for i in range (1,n+1)]
for i in (product(arr, repeat=m)): #can be duplicated
    for j in range(m):
        print(i[j], end=" ")
    print()