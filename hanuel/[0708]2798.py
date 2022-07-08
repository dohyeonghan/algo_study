from itertools import permutations

N, M = map(int, input().split())
CARD = list(map(int, input().split()))
CARD = list(permutations(CARD,3))
MAX = 0
for x,y,z in CARD:
    tmp = x+y+z
    if MAX<tmp and tmp<=M:
        MAX = tmp
print(MAX)