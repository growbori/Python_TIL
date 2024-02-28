T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    if (N% (2*M+1)) == 0:
        answer = N // (2*M+1)
    else:
        answer = N // (2*M+1) + 1

    print(f'#{tc+1} {answer}')