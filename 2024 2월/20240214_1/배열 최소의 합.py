def f(i, k, s):
    global min_sum
    if i == k:
        if min_sum > s:
            min_sum = s

    elif s >= min_sum:
        return
    else:
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            f(i+1, k, s+arr[i][P[i]])
            P[i], P[j] = P[j], P[i]


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = [i for i in range(N)]
    min_sum = 100
    f(0, N, 0)
    print(min_sum)