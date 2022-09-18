from itertools import combinations
import sys
n, k = map(int, input().split())
rm_set = {'a','c','i','n','t'}
alpha = set(chr(i) for i in range(97,123)) - rm_set
# set은 순서 보장 x
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]
def check_cnt(words, check):
    cnt = 0
    for word in words:
        # 체크 변수 위치 제대로 체크하기
        cnt_check = False
        for char in word:
            if check[ord(char)] == 0:
                cnt_check = True
                break
        if cnt_check == False:
            cnt += 1
    return cnt

res = 0
if k >= 5:
    # 알파벳 체크리스트 초기화
    check = [0] * 123
    # 무조건 체크해야하는 rm_set 알파벳 체크
    for c in rm_set:
        check[ord(c)] = 1
    # 가능한 조합 구하기
    for candidate in list(combinations(alpha, k-5)):
        for c in candidate:
            check[ord(c)] = 1
        # 해당 조합에 대해서 카운트
        cnt = check_cnt(words, check)
        res = max(res, cnt)
        # 다음 candidate 넘어가기 전에 리셋
        for c in candidate:
            check[ord(c)] = 0
    print(res)

else:
    print(0)