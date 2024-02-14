def f(i, k, s):     # s는 i-1까지 탐색한 합
    global min_v
    global cnt
    cnt += 2
    if i == k:  # 모든 원소를 고려했니?
        # print(*P)
        if min_v > s:   # 비교하는 순서, 대입하는 순서 맞춰주면 좋음!
            min_v = s
    elif s >= min_v:    # 모든 원소를 고려하지 않았으면 리턴하렴
        return
    else:
        for j in range(i, k):    # P[i] 자리에 바꿀 원소
            P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
            f(i+1, k, s+arr[i][P[i]])   # 순열 자리 결정
            P[i], P[j] = P[j], P[i] # 교환전으로 복구 원상복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100 # 나와있는 모든 수를 더해도 100이 넘지 않음
cnt = 0
f(0, N, 0)
print(min_v, cnt)