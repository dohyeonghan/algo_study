n=int(input())
arr=list(map(int,input().split()))
count=[]

for i in range (n):
    count.append(0)

for i in range (n):
    num=0
    for j in range (1,arr[i]+1):
        if arr[i]%j==0:
            num+=1
        if num==2 and j!=arr[i]:
            count[i]=0
            break #약수 발견 시 포문 종료 => 실행 시간 줄이기
        if num==2 and j==arr[i]:
            count[i]=1

result=0
for i in count:
    if i==1:
        result+=1

print(result)


