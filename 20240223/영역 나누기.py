'''
N*N 칸으로 이뤄진 2차원 배열의 칸에는 1이상 100 이하의 자연수가 들어있다.
행과 행, 열과 열 사이의 직선을 하나씩 그어 A, B, C, D 4개의 영역을 나눴을 때,
각 영역 합의 최대값과 최소값의 차이가 가장 작은 경우를 찾으시오
각 영역은 반드시 한개의 원소를 갖는다
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000000
    for i in range(N-1):    # 영역 나누고
        for j in range(N-1):
            A = 0
            B = 0
            C = 0
            D = 0
            diff = 0
            for x in range(N):    # 탐색
                for y in range(N):
                    if x <= i and y <= j:   # 1사분면
                        A += arr[x][y]

                    elif x <= i and y > j:    # 2사분면
                        B += arr[x][y]

                    elif x > i and y <= j:       # 3사분면
                        C += arr[x][y]

                    else:       #4사분면
                        D += arr[x][y]

            diff = max(A, B, C, D) - min(A, B, C, D)

            if min_sum > diff:
                min_sum = diff
    print(f'#{tc+1} {min_sum}')