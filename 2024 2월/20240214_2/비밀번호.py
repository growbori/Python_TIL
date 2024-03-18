for tc in range(10):
    N, M = input().split()
    stack = []
    new_M = list(M)
    # print(new_M)
    for i in new_M:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    result = ''.join(stack)
    print(f'#{tc+1} {result}')