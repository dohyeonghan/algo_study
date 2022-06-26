n, k = map(int, input().split())
arr = []

for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
    if len(arr)==k:
        print(arr[len(arr)-1])
        break
if len(arr)<k:
    print(0)