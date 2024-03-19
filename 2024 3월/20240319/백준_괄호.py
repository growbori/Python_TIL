dict = {'(' : ')'}

T = int(input())
for tc in range(T):
    arr = input()

    stack= []

    for i in range(len(arr)):
        if len(stack) == 0:
            stack.append(arr[i])
        else:
            if stack[-1] == '(' and arr[i] == ')':
                stack.pop()
            else:
                stack.append(arr[i])

    if len(stack) != 0:
        answer = 'NO'
    else:
        answer = 'YES'

    print(answer)