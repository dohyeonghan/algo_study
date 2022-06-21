k = int(input())
stack = []
for _ in range (k):
    num = int(input())
    stack.append(num) if num!=0 else stack.pop()
print(sum(stack))