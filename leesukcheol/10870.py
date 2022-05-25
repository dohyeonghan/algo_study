n = int(input()) #input method
def fibo(n):
    return fibo(n-1)+fibo(n-2) if n>=2 else 1 if n==1 else 0
print(fibo(n))