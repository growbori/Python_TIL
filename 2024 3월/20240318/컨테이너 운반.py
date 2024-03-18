T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)
    print(weight)
    print(truck)
    delivery = 0

    for i in range(len(weight)):
        for j in range(len(truck)):
            if truck[j] >= weight[i]:
                delivery += weight[i]
                weight[i] = 0
                truck[i] = 0
    print(f'#{tc+1} {delivery}')