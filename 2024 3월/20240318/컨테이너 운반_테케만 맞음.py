'''
N개의 컨테이너를 M 대의 트럭으로 A도시에서 B도시로 이동
트럭당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반 불가능
편도로 한번만 운행, 옮겨진 화물의 전체 무게가 최대가 되도록
컨테이너를 한개도 옮길 수 없는 경우 0을 출력

컨테이너 수 N, 트럭 수 M
화물의 무게, 트럭의 적재용량
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)
    # print(weight)
    # print(truck)
    idx = 0
    for i in weight:
        if i > truck[0]:
            idx += 1
    weight = weight[idx:]
    okay = []
    if N > M:
        for i in range(len(truck)):
            if truck[i] >= weight[i]:
                okay.append(weight[i])
    else:
        for i in range(len(weight)):
            if truck[i] >= weight[i]:
                okay.append(weight[i])
    # print(okay)

    count = 0
    for i in okay:
        count += i

    print(f'#{tc+1} {count}')