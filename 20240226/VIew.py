
for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(2, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2]:
            if arr[i] > arr[i+1] and arr[i] > arr[i+2]:
                count += arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])
    print(count)