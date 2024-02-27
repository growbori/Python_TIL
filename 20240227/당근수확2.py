'''

'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))

    total = 0
    cart = 0
    cnt = 0  # i번 칸에서 0번칸으로 가는 횟수 ( 나중에 *2 해주면 됨)
    for i in range(1, N+1):
        cnt = (A[i] + cart) // M     # 되돌아가는 횟수 (옮긴 횟수)
        cart = (A[i] + cart) % M    # 카트를 옮기고 남은 양 (다음칸에 더해줄 예정)
        # (A[i] + cart) 남은 양
        total += cnt * i    # i에서 x 번째 칸으로 가져간 거리 * 횟수
    if cart > 0:        # 마지막 칸에 당근이 남으면
        total += N


    print(f'#{tc+1} {total*2}') # 왕복 거리 이므로 * 2