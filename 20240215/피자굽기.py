T = int(input())

for tc in range(T):
    N, M = map(int, input().split())    # N은 화덕 크기, M은 피자 갯수
    pizza = list(map(int, input().split()))     # 각 피자의 치즈의 양

    oven = []

    for i in range(N):      # N 개의 피자를 화덕에 넣기 (실제로는 번호만 넣기)
        oven.append(i)

    next = N            # 대기중인 피자 인덱스
    tmp = -1
    while oven:
        tmp = oven.pop(0)   # 입구의 피자(번호)를 꺼내
        pizza[tmp] //= 2    # 한바퀴 회전 후 치즈양
        if pizza[tmp] > 0:  # 치즈가 남은경우 다시 투입 (번호만)
            oven.append(tmp)
        elif next < M:        # 치즈가 다 녹고 다음 피자가 있으면
            oven.append(next)   # 대기중인 피자(번호) 넣기
            next += 1
    print(f'#{tc+1} {tmp+1}')