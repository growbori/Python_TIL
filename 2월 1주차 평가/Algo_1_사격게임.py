def algo(n, arr):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    ans = 0

    for i in range(1, n-1):
        for j in range(1, n-1):

            temp = 0
            for d in range(4):
                temp += arr[i+dx[d]][j+dy[d]]

            sum_score = temp-arr[i][j]

            if sum_score % 2 == 0 and sum_score > 0:
                sum_score *= 2

            if ans < sum_score:
                ans = sum_score

    return ans

T = int(input())
for case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{case} {algo(n, arr)}')