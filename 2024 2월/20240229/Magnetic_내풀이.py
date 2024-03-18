for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    dx = [1]
    dy = [0]

    for i in range(100):
        for j in range(100):
            for p in range(j, 100):
                for k in range(1):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    count = 0
                    for row in arr:
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[i][j] == 1 and arr[nx][ny] == 2:
                                count += 1

    print(count)