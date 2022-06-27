n, m = map(int,input().split())
height = list(map(int,input().split()))
water, left, cnt = 0,0,0
tmp = [0 for _ in range (m)]
for i in range (m):
    if height[i]>left and cnt == 0:
        left = height[i]
    elif i==m-1:
        if height[i]<=height[i-1]:
            break
        water += sum(tmp[i-cnt:i+1]) - cnt*(left-height[i])
    elif height[i]<left:
        tmp[i] += left - height[i]
        cnt+=1
    elif height[i]>=left:
        water += sum(tmp[i-cnt:i+1])
        left = height[i]
        cnt = 0
print(water)


'''
테스트케이스만 통과하네...하
'''