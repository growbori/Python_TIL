T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [N]
    last = 0
    count = 0
    for i in range(1, M+2):
        if (arr[i] - arr[i-1]) <= K:
            if (arr[i] - last) > K:
                last = arr[i-1]
                count += 1
        else:
            count = 0
            break
    print(count)