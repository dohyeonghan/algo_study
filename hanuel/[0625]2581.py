import math

def prime(n):
    if (n<2):
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True

if __name__=="__main__":
    m = int(input())
    n = int(input())
    arr = []
    for j in range(m, n+1):
        if (prime(j)==True):
            arr.append(j)
    print("%d\n%d" %(sum(arr),min(arr)) if arr else -1)
