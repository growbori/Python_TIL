T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    oven = []
    for i in range(N):
        oven.append(i)
    next = N

    # tmp = -1
    while oven :
        index = oven.pop(0)
        pizza[index] //= 2
        if pizza[index] > 0:
            oven.append(index)
        elif next < M:
            oven.append(next)
            next += 1
    print(index+1)