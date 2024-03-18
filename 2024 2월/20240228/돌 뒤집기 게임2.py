T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) # 인덱스 값과 돌의 위치 값을 맞춰주기 위해
    for i in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if i - k > 0 and i + k <= N:
                if arr[i-k] == arr[i+k] == 1:
                    arr[i-k] = 0
                    arr[i+k] = 0
                elif arr[i-k] == arr[i+k] == 0:
                    arr[i-k] = 1
                    arr[i+k] = 1
    print(arr)
    print(f'#{tc+1}', *arr[1:])