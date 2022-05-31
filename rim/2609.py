n1,n2=map(int,input().split())
n1arr=[]
n2arr=[]
for i in range(1,n1+1):
    if n1%i==0:
        n1arr.append(i)
for i in range(1,n2+1):
    if n2%i==0:
        n2arr.append(i)

result1=[]
for i in n1arr:
    if i in n2arr:
        result1.append(i) #가장 큰 max(result1)=최대공약수 출력

print("%i %i" %(max(result1),int((n1*n2)/max(result1)))) #최소공배수 => 두수의 곱=최대공약수*최소공배수
