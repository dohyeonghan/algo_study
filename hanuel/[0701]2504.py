br = input()
stack = []
ans = 0
tmp = 1

for i in range(len(br)):
    if br[i]=='(':
        stack.append(br[i])
        tmp *= 2
    elif br[i]=='[':
        stack.append(br[i])
        tmp *= 3
    elif br[i] == ')':
        if not stack or stack[-1]=='[':
            ans = 0
            break
        if br[i-1]=='(':
            ans += tmp
        stack.pop()
        tmp = tmp//2
    else:
        if not stack or stack[-1]=='(':
            ans = 0
            break
        if br[i-1]=='[':
            ans += tmp
        stack.pop()
        tmp = tmp//3
if stack:
    ans = 0
print(ans)

'''
파이썬은 스택이 없다. 그래서 리스트로 스택을 흉내낸다.
stack = []
stack.append(a) <- push
stack.pop() <- pop (제거한 원소 리턴해줌)
stack[-1] <- top
'''
'''
이 문제는 그냥 논리를 외우는게 맞는듯
'''
