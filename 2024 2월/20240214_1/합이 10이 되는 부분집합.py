def f(i, k, s, t):
    if s == t:
        for j in range(k):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        print()
    elif s > t:
        return
    elif i == k:
        return 
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)


N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N     
f(0, N, 0, 10)