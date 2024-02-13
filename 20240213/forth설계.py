T = int(input())

for tc in range(T):
    A = input().split()
    stack = []

    ans = 0
    for x in A:
        if x.isdigit():     # 피연산자인 경우, 예를 들어 '10'
            stack.append(int(x))    #push
        elif x =='.':
            if len(stack) == 1:# 정상인 경우
                ans = stack.pop()
            else: # error 인 경우
                ans = 'error'
        else:                   # 연산자인 경우,
            # 정상이면 연산 후 push
            # 비정상이면 error

    print(f'#{tc+1} {ans}')


