for tc in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]  # 100*100배열 입력받기
    max_sum = 0
    diagnol_sum1 = 0
    diagnol_sum2 = 0
    for i in range(100):
        row_sum = 0
        col_sum = 0
        for j in range(100):
            row_sum += arr[i][j]  # 같은 행 내의 값 더하기
            col_sum += arr[j][i]  # 같은 열 내의 값 더하기
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
        diagnol_sum1 += arr[i][i]
        diagnol_sum2 += arr[99 - i][i]
    if max_sum < diagnol_sum1:
        max_sum = diagnol_sum1
    if max_sum < diagnol_sum2:
        max_sum = diagnol_sum2

    print(f'#{tc} {max_sum}')