n = int(input())

test = [bin(int(input()))[2:] for _ in range(n)]
for char in test:
    for i in range(len(char)):
        if char[-i-1] == '1':
            print(i, end = ' ')
    print('')