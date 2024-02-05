T = int(input())

for tc in range(T):
    N = int(input())

    count = 0
    nums = [11, 7, 5, 3, 2]

    for num in nums:
        count += N // num
        N %= num

    print(count)