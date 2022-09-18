n,m= map(int, input().split())

n_list = [input() for _ in range(n)]
m_list = [input() for _ in range(m)]
n_dict = {}
for i in range(n):
    n_dict[i+1] = n_list[i]
    n_dict[n_list[i]] = i+1
# print(n_dict)

for i in range(m):
    if m_list[i].isdigit():
        print(n_dict[int(m_list[i])])
    else:
        print(n_dict[m_list[i]])
