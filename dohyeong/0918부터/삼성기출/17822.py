'''
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1

첫째 줄에 N, M, T이 주어진다.

둘째 줄부터 N개의 줄에 원판에 적힌 수가 주어진다. i번째 줄의 j번째 수는 (i, j)에 적힌 수를 의미한다.

다음 T개의 줄에 xi, di, ki가 주어진다.
'''
N, M, T = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int,input().split())) for _ in range(T)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
d_info = [1,-1]
# print(data)
# 회전 정보 동안
temp = [0] * M
# print(temp[1])
# print(info)
for xdk in info:
    xi = xdk[0]
    di = xdk[1]
    ki = xdk[2]
    # 각각 회전
    for i in range(1,N//xi+1):
        # xi * i - 1 : 원판 인덱스
        for j in range(M):
            # print(j)
            # print((j+d_info[di])%4)
            temp[(j+d_info[di]) % 4] = data[xi * i - 1][j]
        # 교환할 temp 완성후
        for j in range(M):
            data[xi*i-1][j] = temp[j]
    # 인접한 것 체크
    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                check = False
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<=ni<N and 0<=nj<M and data[ni][nj] != 0:
                        if data[i][j] == data[ni][nj]:
                            check = True
                            data[ni][nj] = 0
                if check == True:
                    data[i][j] = 0
                else:
                    sum_data = []
                    for x in range(N):
                        for y in range(M):
                            if data[x][y] != 0:
                                sum_data.append(data[x][y])
                    avg = (sum(sum_data)/len(sum_data))
                    for x in range(N):
                        for y in range(M):
                            if data[x][y] != 0:
                                if data[x][y] > avg:
                                    data[x][y] += 1
                                elif data[x][y] < avg:
                                    data[x][y] -= 1

# 다돌았으면 전체 합 구하기
res = 0
for i in range(N):
    for j in range(M):
        res += data[i][j]
print(res)




