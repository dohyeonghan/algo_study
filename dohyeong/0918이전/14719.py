# 투포인터 연습

row, col = map(int, input().split())
graph = list(map(int, input().split()))

left, right = 0, col-1
max_left = graph[left]
max_right = graph[right]

res = 0

while left < right:
    max_left = max(max_left, graph[left])
    max_right = max(max_right, graph[right])

    if max_left >= max_right:
        res += max_right - graph[right]
        right -= 1
    else:
        res += max_left - graph[left]
        left += 1
print(res)