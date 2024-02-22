T = int(input())

for tc in range(T):
    numbers = input()

    split_numbers = [numbers[i:i+7] for i in range(0, len(numbers), 7)]
    # print(split_numbers)
    print(f'#{tc+1}', end = ' ')
    for i in range(len(split_numbers)):
        sum_numbers = 0
        for j in range(7):
            a = int(split_numbers[i][j]) * 2**(7-1-j)
            sum_numbers += a

        print(sum_numbers, end = ' ')
    print()