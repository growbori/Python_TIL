T = int(input())

for tc in range(T):
    n = int(input())
    num_list = [[0] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0
    y = 0
    i = 0
    count = 1
    num_list[0][0] = 1

    while count < n * n:
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or num_list[nx][ny] != 0:
            i = (i+1) % 4
            nx = x + dx[i]
            ny = y + dy[i]

        x = nx
        y = ny
        count += 1
        num_list[nx][ny] = count

    print(f'#{tc+1}')
    for idx in range(n):
        print(*num_list[idx])