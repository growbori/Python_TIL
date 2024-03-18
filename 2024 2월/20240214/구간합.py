T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_list = []
    for i in range(N-M+1):
        sum_num = 0
        for j in range(i, i+M):
            sum_num += arr[j]
        sum_list.append(sum_num)
        sum_list.sort()
        result = sum_list[-1] - sum_list[0]
    print(result)
