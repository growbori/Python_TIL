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

    # print(new)    # 역순으로 뒤집기
    while stack:
        postfix += stack.pop()
    # print(postfix)

    new_stack = []
    for x in postfix:
        if x.isdigit():
            new_stack.append(x)
        else:
            if len(new_stack) >= 2:
                a = new_stack.pop()
                b = new_stack.pop()
                if x == '+':
                    new_stack.append(int(a) + int(b))
                if x == '*':
                    new_stack.append(int(a) * int(b))
    print(new_stack)