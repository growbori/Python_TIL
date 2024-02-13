T = int(input())

def check_l(s):
    stack = []
    for ch in s:
        if ch in '{()}':
            if len(stack):
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
            stack.append(ch)

    if len(stack):
        return 0
    else:
        return 1

for tc in range(T):
    s = input()
    print(f'#{tc+1} {check_l(s)}')