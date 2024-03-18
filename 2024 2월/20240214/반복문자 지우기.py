T = int(input())

for tc in range(T):
    txt = list(input())
    stack = []
    for i in txt:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

    print(f'#{tc+1} {len(stack)}')