'''
굳이 최대 최소를 배열에 넣고 계산할 필요없이 할때마다 체크해주면 됨
필요한 파라미터 : 현재 인덱스(종료조건), 부분합
'''

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_value = 10e9
max_value = -10e9

def dfs(idx, now):
    global min_value, max_value, add, sub, mul, div
    if idx == N:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(idx + 1, now + A[idx])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(idx + 1, now - A[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(idx + 1, now * A[idx])
            mul += 1
        if div > 0:
            div -= 1
            dfs(idx + 1, int(now / A[idx]))
            div += 1

dfs(1,A[0])
print(max_value)
print(min_value)