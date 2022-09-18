import math
n = int(input())
m = int(input())

nums = [i for i in range(n,m+1)]

checks = [True for _ in range(m+1)]
checks[0] = False
checks[1] = False

for i in range(2, int(math.sqrt(m))+1):
    if checks[i] is True:
        j = 2
        while i * j <= m:
            checks[i*j] = False
            j += 1
nums_check = [i for i in range(m+1) if checks[i]]

sum_num = 0

res = [num for num in nums if num in nums_check]

try:
    print(sum(res), min(res), end='\n')
except:
    print(-1)