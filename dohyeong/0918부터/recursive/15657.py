n,m = map(int, input().split())
res =[]
data = list(map(int,input().split()))
data.sort()
def dfs(start):
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(start, len(data)):
        res.append(data[i])
        dfs(i)
        res.pop()
dfs(0)