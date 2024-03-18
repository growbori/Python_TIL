T = int(input())

for tc in range(T):
    txt = list(input())
    stack = []
    top = -1
    for i in txt:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(len(stack))

