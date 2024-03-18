T = int(input())

for tc in range(T):
    A = input().split()
    stack = []
    ans = 0
    for x in A:
        if x in '*/+-':  # 연산자면
            if len(stack) < 2:  #
                ans = 'error'
                break
            else:  # 스택에서 피연산자 두개를 꺼내서 연산 후 다시 push
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
                    div = int(b) // int(a)
                    stack.append(div)
        elif x == '.':
            if len(stack) == 1:  # 정상    (스택에 1개만 있는 경우)
                ans = stack.pop()
            else:  # 비정상 (스택이 비어있거나 2개 이상)
                ans = 'error'
        else:  # 피연산자인 경우
            stack.append(int(x))
    print(f'#{tc + 1} {ans}')