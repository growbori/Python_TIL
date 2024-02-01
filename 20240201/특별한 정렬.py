T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sorting_position = i

        if count % 2 == 1:
            for j in range(i, N):
                if arr[sorting_position] > arr[j]:
                    sorting_position = j
            arr[sorting_position], arr[i] = arr[i], arr[sorting_position]

        else:
            for j in range(i, N):
                if arr[sorting_position] < arr[j]:
                    sorting_position = j
            arr[sorting_position], arr[i] = arr[i], arr[sorting_position]

        count += 1

    print(f'#{tc}', end = ' ')
    print(*arr[0:10])