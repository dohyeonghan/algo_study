from itertools import combinations
n, m = map(int,input().split())
nums = list(map(int, input().split()))
maxnum = 0
candidate = list(combinations(nums, 3))
for i in candidate:
    if sum(i) < m and sum(i)>maxnum: #error. answer is <= ...
        maxnum=sum(i)
print(maxnum)
'''
블랙잭 변형 게임
'''