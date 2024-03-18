for tc in range(10):
    N = int(input())
    A = list(input())
    stack = []
    postfix = ''
    for i in A:
        if i.isdigit():
            postfix += i
        else:
            stack.append(i)
    while stack:
        postfix += stack.pop()

    stack2 = []
    for x in postfix:
        if x.isdigit():
            stack2.append(x)

        else:
            if len(stack2) >= 2:
                a = stack2.pop()
                b = stack2.pop()
                if x == '+':
                    stack2.append(int(a) + int(b))

    print(f'#{tc+1}',*stack2)
