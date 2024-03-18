T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = [0] + list(map(int, input().split())) + [N]

    last = 0
    count = 0
    for i in range(1, M+2):
        if (charger[i] - charger[i-1]) <= K:
            if (charger[i] - last) > K:
                last = charger[i-1]
                count += 1
        else:
            count = 0
            break
    print(count)