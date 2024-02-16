'''
N*N 배열안의 숫자는 해당 영역의 파리 수 의미
한번에 최대한 많은 파리를 죽이고자 함
'''
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    kill_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            kill = 0
            for x in range(M):
                for y in range(M):
                    kill += arr[i + x][j+y]
            kill_list.append(kill)
    print(max(kill_list))

