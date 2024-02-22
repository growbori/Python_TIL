'''
0보다 크고 1 미만인 십진수 N을 이진수로 바꾸려고 한다.
N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외하고 나머지 숫자를 출력
13자리 이상이 필요한 경우에는 'overflow'를 출력하는 프로그램을 작성하시오
'''

T = int(input())
for tc in range(T):
    numbers = float(input())
    binary = ''
    a = 1

    while numbers != 0:
        if (1 / (2 ** a)) <= numbers:
            numbers = numbers - (1 / (2 ** a))      # 기존 값에서 새로운 값으로 갱신
            binary += '1'
        else:
            binary += '0'
        a += 1
        if len(binary) >= 13:       # 소수점 아래 숫자가 13자리 이상일 경우
            binary = 'overflow'
            break
    print(f'#{tc+1} {binary}')
