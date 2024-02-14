T = int(input())

for tc in range(T):
    case = input().split()
    stack = []
    ans = 0
    for x in case:
        if x in '*/+-':
            if len(stack) < 2:
                ans = 'error'
                break
            else:
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
            if len(stack) == 1:
                ans = stack.pop()
            else:
                ans = 'error'
                break
        else:
            stack.append(int(x))
    print(f'#{tc+1} {ans}')