T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    min_num = arr[0]
    max_num = arr[0]

    for i in arr:
        if min_num > i:
            min_num = i

        if max_num < i:
            max_num = i

    print(f'#{tc+1} {max_num - min_num}')