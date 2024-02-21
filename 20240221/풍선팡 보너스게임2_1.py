'''
N * N 격자의 각 칸에 숫자가 고정되어 있다.
어떤 풍선을 터트리면 같은 행과 열의 풍선이 모두 터진다.
터진 풍선에 있던 숫자의 합 중 최대 점수를 출력하라
'''

T = int(input())

for tc in range(T):
    N = int(input())
    ball = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            count = ball[i][j]

            for p in range(1, N+1): # 가로로 쭉! 세로로 쭉 구하기 위한 범위
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += ball[nx][ny]

                    if max_count < count:
                        max_count = count
    print(f'#{tc+1} {max_count}')