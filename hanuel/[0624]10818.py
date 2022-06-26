n = int(input())
arr = list(map(int, input().split()))
min_num = 1000001
max_num = -1000001

for i in arr:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i

print(str(min_num),str(max_num))