def f(i, k):
    global min_v
    global cnt
    cnt += 2
    if i == k:
        # print(*P)
        s = 0   # 선택한 원소의 합
        for j in range(k):  # j 행에 대해
            s += arr[j][P[j]]   # j 행에서 P[j]열을 고른 경우의 합 구하기
        if min_v > s:   # 비교하는 순서, 대입하는 순서 맞춰주면 좋음!
            min_v = s
    else:
        for j in range(i, k):    # P[i] 자리에 바꿀 원소
            P[i], P[j] = P[j], P[i]  # P[i] <-> P[j]
            f(i+1, k)   # 순열 자리 결정
            P[i], P[j] = P[j], P[i] # 교환전으로 복구 원상복구

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
P = [i for i in range(N)]
min_v = 100 # 나와있는 모든 수를 더해도 100이 넘지 않음
cnt = 0
f(0, N)
print(min_v, cnt)