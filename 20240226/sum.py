for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    diagonal_sum = 0
    diagonal_rev_sum = 0
    for i in range(100):
        horizon = 0
        vertical = 0
        for j in range(100):
            horizon += arr[i][j]
            vertical += arr[j][i]

        if max_sum < horizon:
            max_sum = horizon

        if max_sum < vertical:
            max_sum = vertical


        diagonal_sum += arr[i][i]
        diagonal_rev_sum += arr[99-i][i]

    if max_sum < diagonal_sum:
        max_sum = diagonal_sum

    if max_sum < diagonal_rev_sum:
        max_sum = diagonal_rev_sum

    print(max_sum)