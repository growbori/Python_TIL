def f(i, k):
    if i == k:      # 모든 원소에 대해 결정하면
        ss = 0      # 부분집합 원소의 합
        for j in range(k):
            if bit[j]:     # A[i]가 포함된 경우
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

bit = [0] * N     # bit[i]는 A[i]가 부분집합에 포함되는지 표시

f(0, N)