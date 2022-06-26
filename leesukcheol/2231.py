n = int(input())
for num in range (1,n+1):
    nums = [int(k) for k in str(num)]
    candidate = n - sum(nums)
    if candidate == num:
        print(num)
        break
    if num == n:
        print(0)

'''
분배합. 좀 헤맸음.
1부터 n+1까지 하나하나 찾는 느낌으로. 어차피 최솟값을 찾는 문제니까 break를 걸어주면 그게 최솟값이 되니까요?
num의 자릿수를 nums 리스트에 저장했다. 
에러가 계속 났는데, for문 1부터 n+1까지가 아니라 n까지 했고, num==n을 고려하지 않아서 틀렸다.
없을 수도 있다는 걸 생각을 안 했음..
'''
