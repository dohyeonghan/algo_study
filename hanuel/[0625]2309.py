from itertools import combinations

arr = [int(input()) for _ in range(9)]
arr.sort()

for e in list(combinations(arr,7)):
    if sum(e) == 100:
        for x in e:
            print(x)
        break