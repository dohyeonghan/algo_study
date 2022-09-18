from itertools import combinations
import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]

candidate = list(combinations(height, 7))
for c in candidate:
    if sum(c) == 100:
        c = list(c)
        for i in sorted(c):
            print(i)
        break