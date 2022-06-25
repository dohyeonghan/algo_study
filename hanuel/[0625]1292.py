def n_sum(n):
    sum=0
    target=1
    cnt=0
    for _ in range(n):
        if (cnt==target):
            target += 1
            cnt = 0
        cnt += 1
        sum += target
    return sum

if __name__ == "__main__":
    a,b = map(int, input().split())
    print(n_sum(b)-n_sum(a-1)) 