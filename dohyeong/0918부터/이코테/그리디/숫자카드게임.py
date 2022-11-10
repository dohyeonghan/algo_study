n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

tmp = []
for i in range(n):
    tmp.append(min(data[i]))

print(max(tmp))