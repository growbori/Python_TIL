T = int(input())

for tc in range(T):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    sum_list = []
    for i in range(N-M+1):
        sumnum = 0
        for j in range(i, i+M):
            sumnum += arr[j]
        sum_list.append(sumnum)
        sum_list.sort()
    print(sum_list[-1] - sum_list[0])
