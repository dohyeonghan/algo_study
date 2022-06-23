

# 시간초과 코드
# max_sum = -1e9
#
# for i in range(len(data)):
#     if i+k > n:
#         break
#     max_sum = max(max_sum, sum(data[i:i+k]))
# print(max_sum)

# 런타임 에러 코드
# 구간합 구해야함
n,k= map(int, input().split())
data = list(map(int, input().split()))
sum_value = 0
prefix_sum = [0]
for d in data:
    sum_value += d
    prefix_sum.append(sum_value)
# print(prefix_sum)
max_value = -1e9

for i in range(len(prefix_sum)):
    left = i+1
    right = i+k
    if right >= len(prefix_sum):
        break
    max_value = max(max_value, prefix_sum[right] - prefix_sum[left - 1])
print(max_value)


# 세번째 코드
# n,k= map(int, input().split())
# data = list(map(int, input().split()))
# prefix_sum = sum(data[:k])
# res = [prefix_sum]
#
# for i in range(n-k):
#     prefix_sum = prefix_sum - data[i] + data[i+k]
#     res.append(prefix_sum)
# print(max(prefix_sum))
