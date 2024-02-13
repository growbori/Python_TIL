T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                xs, ys = i, j
            if arr[i][j] == 3:
                xe, ye = i, j
    cnt = 0
    stack.append([xs, ys])
    while stack:
        x, y = stack.pop()
        for a in range(4):
            ni = x + di[a]
            nj = y + dj[a]
            if ni == xe and nj == ye:
                cnt += 1
                visited[ni][nj] == 1
                break
            elif 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    stack.append([ni, nj])
                    visited[ni][nj] = 1
    print(f'#{tc} {cnt}')