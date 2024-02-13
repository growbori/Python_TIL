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
        else:
            if len(stack) < 2:  #
                ans = 'error'
                break
            else: # 스택에서 피연산자 두개를 꺼내서 연산 후 다시 push
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    sum = int(b) + int(a)
                    stack.append(sum)
                if x == '-':
                    min = int(b) - int(a)
                    stack.append(min)
                if x == '*':
                    mul = int(b) * int(a)
                    stack.append(mul)
                if x == '/':
                    div = int(b) // int(a)      # 정수형 나눗셈 하기!
                    stack.append(div)            
            # 정상이면 연산 후 push
            # 비정상이면 error

    print(f'#{tc+1} {ans}')


