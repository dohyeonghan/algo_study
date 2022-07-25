n = int(input())
for i in range (0, int(1000000000/6)):
    if n == 1:
        print(1)
        break
    elif 3*i*(i+1)+1 <= n <= 3*(i+1)*(i+2)+1:
        print(i+2)
        break