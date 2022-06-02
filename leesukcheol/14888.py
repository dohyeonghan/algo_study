def dfs(depth, nums, plus, minus, multiple, divide, result):
    global MAX, MIN
    if depth == len(nums)-1:
        MAX = max(MAX, result)
        MIN = min(MIN, result)
        return
    if plus: dfs(depth + 1, nums, plus - 1, minus, multiple, divide, result + nums[depth + 1])
    if minus: dfs(depth + 1, nums, plus, minus - 1, multiple, divide, result - nums[depth + 1])
    if multiple: dfs(depth + 1, nums, plus, minus, multiple - 1, divide, result * nums[depth + 1])
    if divide:
        if result < 0: #음수
            dfs(depth + 1, nums, plus, minus, multiple, divide - 1, (result*(-1) // nums[depth + 1]) * (-1))
        else:
            dfs(depth + 1, nums, plus, minus, multiple, divide - 1, result // nums[depth + 1])
#main
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
MAX = -1e9
MIN = 1e9
dfs(0, nums, ops[0], ops[1], ops[2], ops[3], nums[0])
print("%d\n%d" %(MAX, MIN))