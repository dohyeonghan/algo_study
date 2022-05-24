MAX = 0
current = 0
for _ in range (10):
    OUT , IN = list(map(int,input().split())) #input method
    current += IN - OUT
    if current > MAX:
        MAX = current
print(MAX)