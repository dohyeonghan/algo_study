n,k=map(int,input().split())
list=[]
for i in range(1,n+1):
    if n%i==0:
        list.append(i)
    #k번째 수가 구해졌을 경우, for문에서 나오기
    if len(list)>=k:
        break
if len(list)<k:
    print(0)
else:
    print(list[k-1])