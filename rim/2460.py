sum=0
sumList=[]
for i in range(10):
    num=list(map(int,input().split()))
    sum=sum-num[0]+num[1]
    sumList.append(sum)

print(max(sumList))