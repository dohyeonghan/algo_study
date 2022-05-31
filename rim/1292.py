a,b=map(int,input().split())
arr=[]
for i in range (1,b+1):
    for j in range (1,i+1):
        arr.append(i)

sum=0
for i in range(a-1,b):
    sum=sum+arr[i]

print(sum)