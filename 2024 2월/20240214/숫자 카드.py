T = int(input())

for tc in range(T):
    N = int(input())
    card = list(input())
    c_list = [0] * 10

    for i in range(N):
        c_list[int(card[i])] += 1

    # print(c_list)
    max_count = 0
    max_idx = 0
    for i in range(len(c_list)):
        if max_count <= c_list[i]:
            max_count = c_list[i]
            max_idx = i

    print(f'#{tc+1}', max_idx, max_count)
