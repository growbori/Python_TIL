T = 10
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    apt_list = list(map(int, input().split()))

    for i in range(2, N-2):
        if (apt_list[i] - apt_list[i-1] > 0) and (apt_list[i] - apt_list[i-2] > 0):
            if (apt_list[i] - apt_list[i+1] > 0) and (apt_list[i] - apt_list[i+2] > 0):
                cnt += (apt_list[i] - max(apt_list[i-1], apt_list[i-2], apt_list[i+1], apt_list[i+2]))


    print(cnt)