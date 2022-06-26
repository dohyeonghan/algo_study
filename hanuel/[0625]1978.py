def prime(a):
    if (a<2):
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    for x in arr:
        if prime(x)==True:
            cnt += 1
    print(cnt)