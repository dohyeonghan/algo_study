from itertools import combinations

data = [int(input()) for _ in range(9)]
temp = list(combinations(data, 2))
for i in range(len(temp)):
    res = data[:]
    res.remove(temp[i][0])
    res.remove(temp[i][1])
    if sum(res) == 100:
        res.sort()
        for j in res:
            print(j)
        break
