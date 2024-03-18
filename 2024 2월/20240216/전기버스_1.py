'''
전기 버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대 K 정류장 이동할 수 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇번 충전해야 종점에 갈 수 있는지 구해라
만약 종점에 도착할 수 없다면 0을 출력한다.
'''

T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split()) # 충전기 갯수
    charger = [0] + list(map(int, input().split())) + [N]
    count = 0
    last = 0  # 마지막 충전 위치
    for i in range(1, M+2): # 출발지점, 마지막지점 충전기 있다고 가정해서 +2
        if (charger[i] - charger[i-1]) <=  K: # 충전기 사이에 있으므로 운행 가능
            if (charger[i] - last) > K:     # 마지막 충전기에서 너무 멀면
                last = charger[i-1]
                count += 1

        else:
            count = 0
            break
    print(count)

