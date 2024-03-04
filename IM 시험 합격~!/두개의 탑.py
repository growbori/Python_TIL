T = int(input())
for tc in range(T):
    N, M1, M2 = map(int, input().split())
    arr = list(map(int, input().split()))

    stack1 = []
    arr.sort(reverse=True)
    if M1 > M2:
        # 뽑아내기 1
        for i in range(len(arr)):
            if i % 2 == 0:
                stack1.append(arr[i])
                if len(stack1) == M2:
                    break

        # 뽑아내기 2
        for i in arr:
            for j in stack1:
                if i == j:
                    arr.remove(i)


    if M1 < M2:
        # 뽑아내기 1
        for i in range(len(arr)):
            if i % 2 == 0:
                stack1.append(arr[i])
                if len(stack1) == M1:
                    break

        # 뽑아내기 2
        for i in arr:
            for j in stack1:
                if i == j:
                    arr.remove(i)


    total1 = 0
    for i in range(len(stack1)):
        total1 += stack1[i] * (i+1)
    total2 = 0
    for j in range(len(arr)):
        total2 += arr[j] * (j+1)

    sum_total = total1 + total2
    print(f'#{tc+1} {sum_total}')






