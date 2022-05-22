n, k = map(int, input().split())

candidate = [i for i in range(1,n+1) if n % i == 0]
try:
    print(candidate[k-1])
except:
    print(0)

