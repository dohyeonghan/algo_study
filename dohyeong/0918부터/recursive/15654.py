n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
res = []
def dfs(start):
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(start, len(data)):
        res.append(data[i])
        dfs(i + 1)
        res.pop()

dfs(0)