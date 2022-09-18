a,b,c = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(3)]
max_data = 0
for i in data:
    max_data = max(max_data, i[1])
# print(max_data)

check = [0] * max_data
# print(check)
for i in data:
    for j in range(i[0],i[1]):
        check[j] += 1
# print(check)
# print(check.count(1))
# print(check.count(2))
# print(check.count(3))
print(check.count(1)*a + check.count(2)*2*b + check.count(3) *3 * c)