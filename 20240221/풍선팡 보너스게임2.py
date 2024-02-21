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
    for i in range(N):
        for j in range(N):
            count = ball[i][j]

            for p in range(1, N+1):
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx = i + dx * p
                    ny = j + dy * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += ball[nx][ny]

                    if max_count < count:
                        max_count = count
    print(f'#{tc+1} {max_count}')