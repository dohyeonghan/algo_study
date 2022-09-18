n = input()
sum1, sum2 = 0, 0
for i in n[:len(n)//2]:
    sum1 += int(i)
for i in n[len(n)//2:]:
    sum2 += int(i)

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")