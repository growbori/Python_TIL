T = int(input())
for tc in range(T):
    N = int(input())
    numbers = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = 0
    i = 0
    count = 1
    numbers[0][0] = 1

    while count < N * N:
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or numbers[nx][ny] != 0:
            i = (i+1) % 4
            nx = x + dx[i]
            ny = y + dy[i]

        x = nx
        y = ny
        count += 1
        numbers[nx][ny] = count

    print(f'#{tc+1}')
    for index in range(N):
        print(*numbers[index])


