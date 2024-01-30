T = int(input())

for tc in range(1, T+1):
    n = int(input())
    c = [0] * 12

    for i in range(6):  # 각 자리에 해당 숫자가 몇 개 있는지 조사
        c[n % 10] += 1
        n //= 10

    i = 0
    tri = run = 0

    while i < 10:
        if c[i] >= 3:  # triplet 조사 후 데이터 삭제
            c[i] -= 3  # 2칸 더 만든 이유, run은 뒤에 2개 것을 함께 비교하기 때문에 비교 범위가 n+2 로 늘어남
            tri += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run += 1
            continue
        i += 1

    if run + tri == 2:
        answer = 'Baby Gin'  # run + tri 로 2개가 되어도 성립하고 run만 2개 혹은 tri만 2개여도 성립된다.
    else:
        answer = 'Lose'

    print(f'#{tc} {answer}')