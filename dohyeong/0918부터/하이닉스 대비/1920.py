n = int(input())
A = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

A.sort()
def binary_search(data, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if data[mid] > target:
        return binary_search(data, target, start, mid-1)
    elif data[mid] == target:
        return mid
    else:
        return binary_search(data, target, mid+1, end)


for target in check_list:
    result = binary_search(A, target, 0, len(A)-1)
    if result == None:
        print(0)
    else:
        print(1)