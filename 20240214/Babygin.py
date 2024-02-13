T = int(input())

for tc in range(T):
    number = list(input())
    c = [0] * 12

    for i in range(6):
        c[int(number[i])] += 1


    i = 0
    Tri = Run = 0

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            Tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            Run += 1
            continue
        i += 1

    if Tri + Run == 2:
        answer = 'Baby Gin'

    else:
        answer = 'Lose'

    print(f'#{tc+1} {answer}')

