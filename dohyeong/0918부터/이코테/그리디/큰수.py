n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
total = 0
total += (m //(k+1)) * (data[0]*k+data[1])
total += (m % (k+1)) * data[0]
print(total)