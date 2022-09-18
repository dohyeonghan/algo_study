s = input()

alpha = [i for i in range(97,123)]
s1 = [ord(i) for i in s]
s1.sort()
res = [0] * 26
for i in s1:
    for j in alpha:
        if i == j:
            res[i-97] += 1
for i in res:
    print(i, end=' ')