m = int(input())

arrs = [list(map(int, input().split())) for _ in range(m)]

for arr in arrs:
    res = sorted(arr)[-3]
    print(res)