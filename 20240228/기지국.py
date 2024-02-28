'''
A, B, C의 좌표 찾고 동서남북으로 1, 2, 3 커버하는 기지국 확인
전체 H의 갯수 카운트
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # A 근처 H 'X'로 바꾸기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                        arr[nx][ny] = 'X'
    # print(arr)
    # B 근처 H 'X'로 바꾸기

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                for p in range(1, 3):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p

                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # C 근처 H 'X'로 바꾸기

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'C':
                for p in range(1, 4):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p

                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    #H의 전체 갯수 세기
    count_H = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count_H += 1

    print(f'#{tc+1} {count_H}')