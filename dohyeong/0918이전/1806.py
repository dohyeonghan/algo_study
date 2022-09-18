import sys
n, s = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))
res = 1e9
interval = 0
end = 0
for start in range(n):
    while end < n and interval < s:
        interval += data[end]
        end += 1
    if end == n:
        end -= 1
    res = min(res, end - start)
    interval -= data[start]
print(res)