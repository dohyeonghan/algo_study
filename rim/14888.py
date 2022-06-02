n=int(input())
numbers=list(map(int,input().split()))
symbols=list(map(int,input().split()))
maxResult=-1e9
minResult=1e9


def dfs(i,add,sub,mul,div,nowNum):

    global maxResult,minResult
    if i==n:
        maxResult=max(maxResult,nowNum)
        minResult=min(minResult,nowNum)
        print(maxResult,minResult)
        return
    else:
        if add>0:
            add-=1
            dfs(i+1,add,sub,mul,div,nowNum+numbers[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,add,sub,mul,div,nowNum-numbers[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,add,sub,mul,div,nowNum*numbers[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,add,sub,mul,div,int(nowNum/numbers[i]))
            div+=1



dfs(1,symbols[0],symbols[1],symbols[2],symbols[3],numbers[0])

print(maxResult)
print(minResult)
