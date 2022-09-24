alpha = [chr(i) for i in range(65,91)]
# print(alpha)
data = {i+10 : a for i, a in enumerate(alpha) }
# print(data)
res = []
n, b = map(int, input().split())
while n != 0:
    res.append(n%b)
    n = n // b
res.reverse()
ans = ''
for i in res:
    ans += data[i]
print(ans)
# print(res)
# print(1%2)
# res.append(n%b)
# res.append(n//b)
# res.reverse()
# print(res)
# print(''.join(res.reverse()))