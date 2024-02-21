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
    for i in range(N):
        count = 0
        count2 = 0
        for j in range(M):
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            for p in range(M):
                s1 += fly_map[i][p]  # 행의 합
                s2 += fly_map[p][j]  # 열의 합

            count = s1 + s2 - fly_map[i][j]

            if max_count < count:
                max_count = count

            for p in range(M):
                s3 += fly_map[p][p]
                if 0 <= N - p -1< N:
                    s4 += fly_map[N - p -1][p]

            count2 = s3 + s4 - fly_map[i][j]

            if max_count < count2:
                max_count = count2

    print(max_count)
