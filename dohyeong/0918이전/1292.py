a,b = map(int, input().split())
n = 1
while n * (n+1) <= 2000:
    n += 1
arr = [0]
for i in range(n+1):
    for j in range(i):
        arr.append(i)

print(sum(arr[a:b+1]))