T = 10
for tc in range(1, T + 1):
    input()
    array = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += array[i][j]
        if max_sum < sum:
            max_sum = sum

    for j in range(100):
        sum = 0
        for i in range(100):
            sum += array[i][j]
        if max_sum < sum:
            max_sum = sum
    sum1 = 0
    sum2 = 0
    for i in range(100):
        sum1 += array[i][i]
        sum2 += array[99 - i][i]
    if sum1 > sum2:
        sum = sum1
    else:
        sum = sum2

    if max_sum < sum:
        max_sum = sum

    print(f'#{tc} {max_sum}')