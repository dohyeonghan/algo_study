from itertools import combinations

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
cnt = 0
for i in range(1,n+1):
    data = list(combinations(coins, i))
    for j in data:
        if sum(j) == k:
            cnt += 1
print(cnt)