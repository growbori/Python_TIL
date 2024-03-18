for tc in range(10):
    N, M = input().split()
    stack = []
    top = -1
    for i in range(len(M)):
        if stack:
            if stack[-1] == M[i]:
                stack.pop()
            else:
                stack.append(M[i])
        else:
            stack.append(M[i])

    print(f"#{tc+1} {''.join(stack)}")