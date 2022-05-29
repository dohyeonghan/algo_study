t=int(input())
arr=[] #테스트 케이스 저장할 배열
for i in range(t):
    n=int(input())
    arr.append(n)

for i in range (t):
    temp=format(arr[i], 'b') 
    for j in range(len(temp)-1,-1,-1):
        if temp[j]=='1':
            print(len(temp)-j-1 ,end=" ")
    print()