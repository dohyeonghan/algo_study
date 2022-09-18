from collections import Counter

word = list(input()) # str을 리스트로 받아서 sort하기
word.sort() # 오름차순 출력을 위해 미리 sort
# print(word)
word_count = Counter(word) # Counter 객체로 개수 카운트
# print(word_count)
odd_count = 0 # 홀수개인 요소가 2개이상이면 팰린드롬 자체를 만들 수가 없으므로 홀수 개수 체크용
odd_center = '' # 홀수개인 요소가 한개면 해당 값이 센터에 와야함
for key, value in word_count.items(): # 카운터 객체 키 밸류 둘다 순회하면서
    if value % 2 != 0: # 홀수개면
        odd_count += 1 # 홀수 카운트
        if odd_count > 1: # 센터에 넣기 전에 홀수가 두개이상이면 break해서 빠져나가기
            break
        odd_center += key # 센터 값 지정하기
        word.remove(key) # 센터 값으로 지정했으면 word에서는 빼주기 -> 짝수개만 남음
if odd_count > 1: # 홀수가 두개이상이면 실패
    print("I'm Sorry Hansoo")
else:
    left = '' # 센터기준 왼쪽에 들어갈 문자열 지정
    for i in range(0,len(word),2): # 2개씩 건너뛰면 반으로 나눈것과 같음
        left += word[i] # word에 해당하는 인덱스 값 지정해서 left에 넣어주기
    print(left + odd_center + left[::-1]) # left와 left 반대로 만든것, 센터까지 합쳐서 팰린드롬 생성

