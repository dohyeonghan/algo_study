n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
# 식의 결과 10억기준
min_sum = 1e9
max_sum = -1e9
def calculator(depth, sum):
    global min_sum, max_sum
    if depth == n:
        min_sum = min(min_sum, sum)
        max_sum = max(max_sum, sum)
        return min_sum, max_sum
    # op + - * //
    else:
        if op[0] > 0:
            op[0] -= 1
            calculator(depth+1, sum + a[depth])
            op[0] += 1
        if op[1] > 0:
            op[1] -= 1
            calculator(depth+1, sum-a[depth])
            op[1] += 1
        if op[2] > 0:
            op[2] -= 1
            calculator(depth+1, sum * a[depth])
            op[2] += 1
        if op[3] > 0:
            op[3] -= 1
            calculator(depth+1, int(sum/a[depth]))
            op[3] += 1

calculator(depth=1, sum=a[0])
print(max_sum)
print(min_sum)