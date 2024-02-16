'''
1-9 로 구성된 6개의 숫자를 읽어 베이비진을 판단하시오
'''

T = int(input())
for tc in range(T):
    numbers = list(input())

    check = [0] * 12
    tri = run = 0
    for i in range(len(numbers)):
        check[int(numbers[i]) % 10] += 1

    for i in range(len(check)):
        if check[i] >= 3:
            check[i] -= 3
            tri += 1

        if check[i] >= 1 and check[i+1] >= 1 and check[i+2] >= 1:
            check[i] -= 1
            check[i+1] -= 1
            check[i + 2] -= 1
            run += 1

    if run + tri == 2:
        answer = 'Baby Gin'
    else:
        answer = 'Lose'

    print(answer)
