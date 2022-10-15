# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
S = 'aabbcc'
C = [1,2,1,2,1,2]
def solution(S, C):
    target = S[0]
    tmp_cost = [C[0]]
    cost_cnt = 1
    res = 0
    for i in range(len(S)-1):
        if S[i + 1] != target:
            if cost_cnt == 1:
                target = S[i + 1]
                tmp_cost = [C[i + 1]]
                continue
            else:
                target = S[i + 1]
                tmp_cost.sort()
                res += sum(tmp_cost[0:-1])
                tmp_cost = [C[i + 1]]
                cost_cnt = 1

        else:
            cost_cnt += 1
            tmp_cost.append(C[i + 1])
            if i+1 == len(S)-1:
                tmp_cost.sort()
                res += sum(tmp_cost[0:-1])

    return res

print(solution(S,C))