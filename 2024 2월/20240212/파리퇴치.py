T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    num_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            summ = 0
            for x in range(M):
                for y in range(M):
                    summ += arr[i+x][j+y]
            num_list.append(summ)
            max_sum = max(num_list)
    print(max_sum)

