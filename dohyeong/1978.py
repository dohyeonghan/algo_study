import math, sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
cnt = 0
checks = [True for _ in range(1001)]
checks[0] = False
checks[1] = False

for i in range(2, int(math.sqrt(1000))+1):
    if checks[i] is True:
        j = 2
        while i * j <= 1000:
            checks[i*j] = False
            j += 1

nums_check = [i for i in range(1001) if checks[i]]

for num in nums:
    if num in nums_check:
        cnt += 1
print(cnt)