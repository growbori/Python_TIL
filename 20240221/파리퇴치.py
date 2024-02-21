'''
N * N 배열에서 M*M 배열 크기의 파리채로 파리를 퇴치한다.
최대로 퇴치할 수 있는 파리의 수를 구하여라
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            fly_sum = 0
            for x in range(M):
                for y in range(M):
                    fly_sum += arr[i + x][j + y]

            if max_sum < fly_sum:
                max_sum = fly_sum

    print(f'#{tc+1} {max_sum}')