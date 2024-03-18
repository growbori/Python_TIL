'''
전기 카트로 사무실을 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
각 구역을 한번씩만 방문하고, 사무실로 돌아올 때 최소 배터리 사용량을 구하시오
1번은 사무실, 2번부터 N번은 관리구역 번호이다.
칸에 들어가는 숫자가 0일 경우 계산 x
순열로 갈수 있는 경우의 수 구하고, 그 경우에 수에 맞는 인덱스 값들 더하기
'''

def f1(i, k):
    global min_v
    if i == k:
        # p 순서로 방문 했을때 비용
        # print(p) # 방문하는 순서 정하기
        s = e[0][p[0]-1]    # 사무실에서 첫번째 관리 구역
        for j in range(1, k):   # 관리구역 사이
            s += e[p[j-1]-1][p[j]-1]
        s += e[p[k-1]-1][0]
        if min_v > s:
            min_v = s
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                f1(i+1, k)
                used[j] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]     # 배터리 소비량
    min_v = 10000
    arr = [i for i in range(2, N+1)]
    used = [0]* (N-1)       # 사무실 제외
    p = [0] * (N-1)
    f1(0, N-1)    # 0부터 총 갯수 N-1까지

    print(f'#{tc+1} {min_v}')