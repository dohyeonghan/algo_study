H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
for i in range(1,H+1):
    left = False
    right = False
    start=1
    for j in range(W+1):
        if j==W:
            if left == True and right == True:
                for k in range(start,j):
                    if block[k]<i:
                        ans+=1
        elif block[j]<i and left==True and right == True:
            if left==True and right == True:
                for k in range(start,j):
                    if block[k]<i:
                        ans+=1
                        right=False
                start=j
        elif block[j]>=i and left==True:
            right=True
        elif block[j]>=i and left==False:
            left=True
        else:
            pass
print(ans)

'''
흑흑 분명 테스트케이스랑 반례는 다 통과하는데
자꾸 틀렸다고하네...
'''
'''
이 사람은 천재인가봐!!
h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare:
        ans += compare - world[i]

print(ans)
'''