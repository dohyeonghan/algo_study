import sys
n = int(sys.stdin.readline())
stack = []
for _ in range (n):
    message = sys.stdin.readline().split() #push, pop, size, empty, top -> in message[0]
    if message[0] == 'push': stack.append(message[1])
    elif message[0] == 'pop': print(-1) if len(stack)==0 else print(stack.pop())
    elif message[0] == 'size': print(len(stack))
    elif message[0] == 'empty': print(int(len(stack)==0))
    elif message[0] == 'top':
        print(-1) if len(stack)==0 else print(stack[-1])
        
        
'''
stack. 1
'''