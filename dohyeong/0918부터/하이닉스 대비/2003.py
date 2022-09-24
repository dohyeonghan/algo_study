n, m = map(int, input().split())
data = list(map(int, input().split()))

temp = 0
end = 0
cnt = 0

for start in range(n):
    while end < n and temp < m:
        temp += data[end]
        end += 1
    if temp == m:
        cnt += 1
    temp -= data[start]
print(cnt)