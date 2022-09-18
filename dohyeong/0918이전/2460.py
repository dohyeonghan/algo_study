data = [list(map(int, input().split())) for _ in range(10)]

res = data[0][1]
p = data[0][1]
for i in range(1,10):
    p += data[i][1] - data[i][0]
    res = max(res, p)
print(res)