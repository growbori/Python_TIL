T = int(input())

for tc in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    minidx = 0
    maxidx = 0

    for i in range(n):
        if arr[i] < arr[minidx]:
            minidx = i

        if arr[i] >= arr[maxidx]:
            maxidx = i

    print(abs(maxidx - minidx))