T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum = []
    for i in range(N-1):
        a = arr[i]
        for j in range(i+1, N):
            b = arr[j]
            sum.append(a+b)
            sum.sort()
    # print(sum)
    total = []
    for i in range(len(sum)):
        if sum[i] <= M:
            total.append(sum[i])

    answer = -1
    if len(total) != 0:
        answer = max(total)

    print(f'#{tc+1} {answer}')
