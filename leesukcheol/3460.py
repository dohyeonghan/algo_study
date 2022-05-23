T = int(input()) #input method
for _ in range (T):
    n = int(input())
    n = str(bin(n))[:1:-1]
    for i in range (len(n)):
        if n[i] == '1':
            print(i, end=" ")
    print()