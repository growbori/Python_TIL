def f(i, j, N, s):      # i, j 칸에 진입, s 지나온 칸의 합계
    global min_v
    global cnt
    cnt += 1
    if i >= N or j >= N:    #   배열을 벗어나는 경우
        return
    elif i == N-1 and j == N-1:
        if min_v > s + arr[N-1][N-1]:   # 마지막 칸을 포함한 합계가 최소인 경우
            min_v = s + arr[N-1][N-1]
        return
    elif s >= min_v:    # 가지치기!
        return
    else:
        if i + 1 < N:
            f(i + 1, j, N, s + arr[i][j])
        if j + 1 < N:
            f(i, j + 1, N, s + arr[i][j])
        # global s 사용하지 않기



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 4000        # 모든 칸을 다 지나도 이 이상 넘지 않음
    cnt = 0
    f(0, 0, N, 0)
    print(f'#{tc} {min_v} {cnt}')