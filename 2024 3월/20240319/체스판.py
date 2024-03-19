'''
파리퇴치 + delta
8*8크기보다 체스판이 큰 경우 체스판을 자른다!
이때 다시 칠하는 정사각형의 갯수가 최소가 되도록 구해라
'''


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

# print(arr)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0
# 체스판의 크기가 8*8인 경우
if N== 8 and M == 8:
    for i in range(N):
        for j in range(M):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and arr[i][j] == arr[nx][ny]:
                    if arr[i][j] == 'W':
                        arr[nx][ny] = 'B'
                        count += 1
                    elif arr[i][j] == 'B':
                        arr[nx][ny] = 'W'
                        count += 1
                answer =count
# 체스판의 크기가 8*8 보다 큰 경우
else:
    min_count = 10000
    for x in range(N-8+1):
        for y in range(M-8+1):
            count = 0
            for i in range(x, x+8):
                for j in range(y, y+8):
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and arr[i][j] == arr[nx][ny]:
                            if arr[i][j] == 'W':
                                arr[nx][ny] = 'B'
                                count += 1
                            elif arr[i][j] == 'B':
                                arr[nx][ny] = 'W'
                                count += 1
                        if min_count > count:
                            min_count = count

                        answer = min_count
print(answer)