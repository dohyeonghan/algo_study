t = int(input())

for i in range(t):
    n = int(input())
    k = 0
    while(n!=0):
        if n%2==1:
            print(k, end=" ")
        n = n//2
        k+=1