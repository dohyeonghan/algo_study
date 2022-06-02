M = int(input())
N = int(input())
primes = []
for i in range(M, N+1):
    if i != 1: 
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check: primes.append(i)
print("%d\n%d" %(sum(primes), min(primes))) if primes else print(-1)


'''m = int(input())
n = int(input())
primes = []
for i in range(m, n+1):
    if m==1 and n==1: break
    for j in range (1,int(i**5)+1):
        if i%j==0: break
    else : primes.append(i)
print("%d\n%d" %(sum(primes), min(primes))) if primes else print(-1)'''