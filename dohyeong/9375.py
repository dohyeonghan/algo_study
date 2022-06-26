from collections import defaultdict
n = int(input())
res = []
for _ in range(n):
    m = int(input())
    temp = 1
    data = [list(input().split()) for _ in range(m)]
    data_dict = defaultdict(list)
    for d in data:
        data_dict[d[1]].append(d[0])
    for key in data_dict.keys():
        temp *= (len(data_dict[key]) + 1)
    res.append(temp)
for i in res:
    print(i-1)

