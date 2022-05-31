a, b = list(map(int, input().split())) #input method
numbers = []
for i in range (46): #1000을 넘는 시점이 i=45
    for j in range (i):
        numbers.append(i)
print(sum(numbers[a-1:b]))