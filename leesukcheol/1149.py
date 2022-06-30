n = int(input())
hs = []
for _ in range (n): hs.append(list(map(int, input().split())))
for i in range (1,n):
    hs[i][0] = min(hs[i-1][1],hs[i-1][2]) + hs[i][0]
    hs[i][1] = min(hs[i-1][0],hs[i-1][2]) + hs[i][1]
    hs[i][2] = min(hs[i-1][0],hs[i-1][1]) + hs[i][2]
print(min(hs[n-1]))