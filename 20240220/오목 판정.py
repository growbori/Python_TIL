'''
N * N 크기의 판 가로, 세로 대각선 중 하나의 방향으로 다섯개 이상 연속
'''


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    omok = 0
    diagonal = ''
    diagonal_reverse = ''
    for i in range(N):
        vertical = ''
        horizon = ''
        for j in range(N):
            vertical += arr[i][j]
            if vertical == 'ooooo':
                omok += 1

            horizon += arr[j][i]
            if horizon == 'ooooo':
                omok += 1

        diagonal += arr[i][i]
        if diagonal == 'ooooo':
            omok += 1

        diagonal_reverse += arr[N-1- i][i]
        if diagonal_reverse == 'ooooo':
            omok += 1

    if omok >= 1:
        answer = 'YES'
    else:
        answer = 'NO'


    print(f'#{tc+1} {answer}')