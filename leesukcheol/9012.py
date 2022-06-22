t = int(input())
for _ in range (t):
    stack = []
    ps = input()
    for i in ps:
        stack.append(i)
        if len(stack)>=2 and stack[-1]==')' and stack[-2]=='(':
            stack.pop()
            stack.pop()
    print("YES") if len(stack)==0 else print("NO")