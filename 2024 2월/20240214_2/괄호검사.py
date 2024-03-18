op = {')' : '(', '}' : '{'}

T = int(input())
for tc in range(T):
    s = list(input())
    stack = []
    ans = 1
    for i in s:
        if i in '{(':
            stack.append(i)
        elif i in '})':
            if not stack:
                ans = 0
                break
            else:
                t = stack.pop()
                if t != op[i]:
                    ans = 0
    else:
        if stack:
            ans = 0

    print(ans)
