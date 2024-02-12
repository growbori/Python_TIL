T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = int(input())
    c = [0] * 12
    max_count = 0
    for i in range(N):
        c[arr %10] += 1
        arr //= 10

    for a in c:
        if a >= max_count:
            max_count = a

    max_num = c[0]
    max_idx = 1

    for j in range(10):
        if c[j] >= max_num:
            max_num = c[j]
            max_idx = j

    print(max_idx, max_count)