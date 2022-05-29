member=[]
answer=[]
for i in range(9):
    num=int(input())
    member.append(num)

def dfs(n,list):
    if len(list) == 7 and sum(list)==100:
        answer.append(list[:])
        return
    for i in range (n,9):
        dfs(i+1,list+[member[i]])
        
dfs(0,[])

answer[0].sort()
for i in answer[0]:
    print(i)