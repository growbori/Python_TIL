for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    diagonal_sum = 0
    diagonal_reverse_sum = 0

    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        if max_sum < row_sum:
            max_sum = row_sum

        if max_sum < col_sum:
            max_sum = col_sum

        diagonal_sum += arr[i][i]
        diagonal_reverse_sum += arr[99-i][i]

    if max_sum < diagonal_sum:
        max_sum = diagonal_sum
    if max_sum < diagonal_reverse_sum:
        max_sum = diagonal_sum

    print(f'#{tc+1} {max_sum}')