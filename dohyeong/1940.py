# 시간초과 코드

# n = int(input())
# m = int(input())
# nums = list(map(int, input().split()))
# cnt = 0
# if m > 200000: # 예외처리
#     print(0)
# else:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == m:
#                 cnt += 1
#     print(cnt)

# 투포인터 -> 정렬후 사용
n = int(input())
m = int(input())
nums = list(map(int, input().split()))
cnt = 0
left = 0
right = n-1
nums.sort()
while left < right:
    if nums[left] + nums[right] == m:
        cnt += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] < m:
        left +=1
    else:
        right -= 1
print(cnt)