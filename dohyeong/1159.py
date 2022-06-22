from collections import defaultdict
n = int(input())

data = [input() for _ in range(n)]
# print(data)
candidates = defaultdict(list)
for d in data:
    candidates[d[0]].append(d)
# print(candidates)
res = []
for key in candidates.keys():
    if len(candidates[key]) >= 5:
        res.append(key)
if len(res) > 0:
    res.sort()
    for i in res:
        print(i, end='')
else:
    print('PREDAJA')