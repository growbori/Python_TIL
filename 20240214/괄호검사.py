T = int(input())
for tc in range(T):
    sample = input()

    cnt = 0
    for _ in sample:
        cnt += 1
    N = cnt
    stk = []

    for char in sample:
        if char == '{' or char == '(':
            stk += char

        elif char == '}':
            if stk != [] and stk[-1] == '{':
                stk.pop()
            else:
                stk += char

        elif char == ')':
            if stk != [] and stk[-1] == '(':
                stk.pop()
            else:
                stk += char

    if stk:
        print(f'#{tc+1} 0')

    else:
        print(f'#{tc+1} 1')