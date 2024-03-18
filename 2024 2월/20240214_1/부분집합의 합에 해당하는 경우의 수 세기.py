def f(i, k, s, t):
    global cnt

    if s == t:
        for j in range(k):
            if bit[j]:
                s += A[j]
                print(A[j], end = ' ')
        cnt +=1
        print()

    elif i == k:
        return

    elif s > t:
        return

    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)

N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * N
cnt = 0
f(0, N, 0, 10)
print('cnt : ', cnt)