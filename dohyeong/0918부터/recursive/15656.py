n,m = map(int, input().split())
res =[]
data = list(map(int,input().split()))
data.sort()
def dfs():
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(len(data)):
        res.append(data[i])
        dfs()
        res.pop()
dfs()