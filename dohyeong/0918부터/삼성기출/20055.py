'''
2 ≤ N ≤ 100
1 ≤ K ≤ 2N
1 ≤ Ai ≤ 1,000
'''

n, k = map(int, input().split())

belt = list(map(int, input().split()))
robot = [0] * n
# print(belt)
# print(robot)
def rotate_arr(arr):
    tmp = [0] * len(arr)
    i = 0
    while True:
        if i <= len(arr)-2:
            tmp[i+1] = arr[i]
            i+=1
        else:
            tmp[0] = arr[-1]
            break
    return tmp
# print(rotate_arr(belt))
# print(rotate_arr(robot))
res = 0
while True:
    belt = rotate_arr(belt)
    robot = rotate_arr(robot)
    robot[-1] = 0

    if sum(robot) > 0:
        for i in range(n-2, -1, -1):
            if robot[i] == 1 and belt[i+1] > 0 and robot[i+1] == 0:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1
        robot[-1] = 0

    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    res += 1
    if belt.count(0) >= k:
        break
print(res)



