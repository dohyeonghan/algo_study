N = int(input())
inputs = list(map(int, input().split())) #input method
primes = [True for _ in range (1001)] #Eratosthenes sieve
for i in range(2, int(1000**0.5)+1):
    if primes[i] == True:
        j = 2
        while i * j <= 1000:
            primes[i * j] = False
            j += 1
primes = [i for i in range (2, 1001) if primes[i]]
for i in inputs:
    if i not in primes:
        N-=1
print(N)