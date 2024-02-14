def f(i, k):
    if i == k:
        ss = 0
        for j in range(k):
            if bit[j]:
                # print(A[j], end = ' ')
                ss += A[j]
        print(ss)
    else:
        for j in range(1, -1, -1):
            bit[i] = j
            f(i+1, k)
        # bit[i] = 1
        # f(i+1, k)
        # bit[i] = 0
        # f(i+1, k)
N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N)