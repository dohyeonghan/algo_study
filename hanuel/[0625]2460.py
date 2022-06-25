a, b = map(int, input().split())
sum = b
max = -1

while(b != 0):
    a, b = map(int, input().split())
    sum = sum - a + b
    if max<sum:
        max = sum
print(max)