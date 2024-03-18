'''
100 * 100 2차원 배열
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 것
동일한 최댓값이 있을 경우 하나만 출력
'''
for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    diagonal_sum = 0
    diagonal_reverse_sum = 0
    max_sum = 0
    sum_list = []
    for i in range(100):
        col_sum = 0
        row_sum = 0
        for j in range(100):
            col_sum += arr[i][j]
            row_sum += arr[j][i]
        if max_sum < row_sum:
            max_sum = row_sum
        if max_sum < col_sum:
            max_sum = col_sum
            diagonal_sum += arr[i][i]
            diagonal_reverse_sum += arr[99-i][i]

        if max_sum < diagonal_sum:
            max_sum = diagonal_sum
        if max_sum < diagonal_reverse_sum:
            max_sum = diagonal_reverse_sum

    print(max_sum)
