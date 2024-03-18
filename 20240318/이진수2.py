# 이진수 소수점 값의 합이 나오도록

T = int(input())
for tc in range(T):
    numbers = float(input())
    binary = ''
    a = 1

    while numbers != 0:
        if (1/(2**a)) <= numbers:
            numbers = numbers - (1/(2**a))
            binary += '1'
        else:
            binary += '0'
        a += 1

        if len(binary) >= 13:
            binary = 'overflow'
            break
    print(f'#{tc+1} {binary}')