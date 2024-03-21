T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    mask = 1    # 비교연산
    ans = 1     # 결괏값
    for _ in range(N):
        if M & mask == 0:
            ans = 0
            break
        mask = mask << 1

    if ans == 1:
        answer = 'ON'
    else:
        answer = 'OFF'

    print(f'#{tc+1} {answer}')