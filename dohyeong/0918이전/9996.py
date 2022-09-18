n = int(input())
check = input()
data = [input() for _ in range(n)]

for i in range(len(check)):
    if check[i] == '*':
        star = i
pre = check[0:star]
suf = check[star+1:]
# 반례 주의 ab*ab -> ab
for d in data:
    if len(d) >= len(pre) + len(suf):
        if d[0:len(pre)] == pre and d[len(d)-len(suf):] == suf:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")