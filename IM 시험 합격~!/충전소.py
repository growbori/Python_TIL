T = int(input())
for tc in range(T):
    N = int(input())
    Xh, Yh, D = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * 30 for _ in range(30)]

    for i in range(30):
        for j in range(30):
            Xh = Xh + 15
            Yh = Yh + 15
            if Xh == i and Yh == j:
                board[i][j] = 'H'

    print(board)

