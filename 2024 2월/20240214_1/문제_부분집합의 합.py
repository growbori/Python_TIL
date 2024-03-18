def f(i, k, N, M):
    global cnt

    if i == k:
        part = []
        for j in range(k):
            if bit[j]:
                part.append(A[j])
        if len(part) == N and sum(part) == M:
            cnt += 1

    else:
        bit[i] = 1
        f(i+1, k, N, M)
        bit[i] = 0
        f(i+1, k, N, M)


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bit = [0] * 12
    cnt = 0
    f(0, 12, N, M)
    print(f'#{tc+1} {cnt}')