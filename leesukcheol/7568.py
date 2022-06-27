n = int(input())
people = []
grades = [1 for _ in range (n)]
for _ in range (n): people.append(list(map(int, input().split())))
for i in range (n):
    for j in range (n):
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]: grades[i]+=1 #evaluate the grade each other
for grade in grades: print(grade, end=" ")

'''
덩치. for _에서 set로 안 하고 list로 한 이유: set로 하니까 몸무게 키가 뒤바뀔 수 있음ㅋㅋ
grades에 0을 채워넣고 등급 부여할 때 >=로 했는데 바로 오류떴음.
생각해보니 모두 같으면 1등이 아니라 5등이 뜸... 그래서 바로 1, >로 바꿈
'''