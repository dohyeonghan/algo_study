n = int(input())
houses = []
answer = 0
before = -1
for _ in range (n):
    houses.append(list(map(int,input().split())))
for i in range (n):
    if before>=0:
        houses[i][before] = max(houses[i])+1
        tmp = houses[i].index(min(houses[i]))
        answer += houses[i][tmp]
        before = tmp
    elif houses[i][0]==houses[i][1]==houses[i][2]:
        #before = houses[i].index(min(houses[i]))
        answer += min(houses[i])
    else:
        before = houses[i].index(min(houses[i]))
        answer += min(houses[i])
print(answer)

'''
히든도 찾은 것 같은데 왜 도대체?
'''