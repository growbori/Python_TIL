T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    minnum = 10
    maxnum = 0
    min_idx = 0
    max_idx = 0
    for i in range(len(arr)):
        if minnum > arr[i]:
            minnum = arr[i]
            min_idx = i

        if maxnum <= arr[i]:
            maxnum = arr[i]
            max_idx = i
    print(f'#{tc+1} {abs(max_idx - min_idx)}')