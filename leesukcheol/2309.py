import itertools
height = [int(input()) for _ in range (9)]
temp = list(itertools.combinations(height, 7))
for i in temp:
    if sum(i)==100:
        for j in sorted(list(i)):
            print(j)
        break