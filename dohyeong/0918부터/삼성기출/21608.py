n = int(input())
student = [list(map(int, input().split())) for _ in range(n**2)]
graph = [[0] * n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 좋아하는 학생과 빈칸 인근에 있는지 확인
for s in student:
    data = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<=ni<n and 0<=nj<n:
                        if graph[ni][nj] in s[1:]:
                            like += 1
                        if graph[ni][nj] == 0:
                            blank += 1
                data.append([like, blank, i, j])
    data.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # print(data)
    # print(data)
    res = data[0]
    graph[res[2]][res[3]] = s[0]
# 학생 만족도 구하기
student.sort(key=lambda x: x[0])
res = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni<n and 0<=nj<n:
                if graph[ni][nj] in student[graph[i][j]-1][1:]:
                    cnt += 1
        if cnt > 0:
            res += 10**(cnt-1)
print(res)