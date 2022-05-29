T = int(input()) #Test case
arr = "" #arr type: str
for _ in range (T):
    arr = input().split(' ') #arr type: str -> list
    arr = [int(i) for i in arr] #element type: str -> list
    print(sorted(arr)[-3])
'''
input method에서 map 함수를 못 쓴다고 생각하고 풀어봄
list(map(int, input().split()))을 못 쓸 때 어떻게 해야 할지...를 생각하다가
저렇게 해봤음. 코드 한 줄이 3줄이 되는 마법
'''