T = int(input())
for tc in range(T):
    A, B, C, D = map(int, input().split())

    # 먼저 꺼진 시간이 나중에 켜진것보다 길면 먼저 꺼진 시간에서 나중에 켜진 시간을 빼면 된다.
    answer = 0
    OFF = min(B, D)
    ON = max(A, C)

    if OFF > ON:
        answer = OFF - ON

    print(f'#{tc + 1} {answer}')