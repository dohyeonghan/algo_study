from itertools import combinations
import sys
n, k = map(int, input().split())
input = sys.stdin.readline
words = [input() for _ in range(n)]
candidates = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
res = 0

if 5<k<=26:
    alpha_list = list(combinations(candidates, k-5))
    for alphas in alpha_list:
        alphas = list(alphas)
        alphas.extend(['a','n','t','c','i'])
        tmp = 0
        for word in words:
            check = False
            for char in word[4:-4]:
                if char not in alphas:
                    check = True
                    break
            if check == False:
                tmp += 1
        res = max(res, tmp)
    print(res)
elif k == 5:
    check = False
    for word in words:
        if len(word) == 8:
            check = True
    if check == True:
        print(1)
    else:
        print(0)
else:
    print(0)



