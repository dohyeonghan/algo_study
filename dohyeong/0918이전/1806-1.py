import sys
n, s = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))
res = 100001
interval = 0
end = 0
start = 0
while True:
    if interval >= s:
        res = min(res, end-start)
        interval -= data[start]
        start += 1
    elif end == n:
        break
    else:
        interval += data[end]
        end += 1
if res == 100001:
    print(0)
else:
    print(res)
