T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())  # K 최대 이동거리, N 종점번호, 충전기 개수
    charger = [0] + list(map(int, input().split())) + [N]

    last = 0  # 마지막 충전위치, 초기값은 출발점 0\
    count = 0  # 충전횟수
    for i in range(1, M + 2):  # 모든 충전기 위치 charger[i]에 대해
        if (charger[i] - charger[i - 1]) <= K:  # 충전기 사이 운행 가능
            if (charger[i] - last) > K:  # 마지막충전기에서 너무 멀면
                last = charger[i - 1]
                count += 1
        else:
            count = 0
            break
    print(f'#{tc} {count}')



