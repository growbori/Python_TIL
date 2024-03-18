'''
N * N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수 의미
파리 킬러 스프레이를 한번만 뿌려 최대한 많은 파리를 잡으려고 함
+ 혹은 x 형태로 분사됨
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    fly_map = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ux = [1, 1, -1, -1]
    uy = [-1, 1, 1, -1]

    for i in range(N):
        for j in range(N):
            count = fly_map[i][j]

            for p in range(1, M):
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += fly_map[nx][ny]

            if max_count < count:
                max_count = count

            count = fly_map[i][j]
            for p in range(1, M):
                for k in range(4):
                    nx = i + ux[k] * p
                    ny = j + uy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += fly_map[nx][ny]

            if max_count < count:
                max_count = count
    print(f'#{tc+1} {max_count}')