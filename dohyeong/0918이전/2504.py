data = input()
stack = []
tmp = 1
res = 0

for i in range(len(data)):
    # 열때 : 스택 append
    if data[i] == '(':
        tmp *= 2
        stack.append(data[i])
    elif data[i] == '[':
        tmp *= 3
        stack.append(data[i])

    # 닫을 때 : 조건 맞는지 확인, 직전 인덱스 확인
    elif data[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        # 직전 인덱스면 제일 내부
        if data[i-1] == '(':
            res += tmp
        # 다 빠져나왔을 때 or 이중삼중 겹쳐 있을 때는 tmp 나눠줘야 초기화 가능
        tmp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        if data[i-1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()
if stack:
    res = 0
print(res)