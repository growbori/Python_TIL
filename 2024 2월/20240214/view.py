for tc in range(10):
    T = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, T-1):
        if (arr[i] > arr[i-1]) and (arr[i] > arr[i-2]) :
            if (arr[i] > arr[i+1]) and (arr[i] > arr[i+2]):
                cnt += arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])

    print(f'#{tc+1} {cnt}')