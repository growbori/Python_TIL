def f(i, k, s, t): # k 개의 원소를 가진 배열A, 부분집합의 합이 t인 경우
    global cnt
    cnt += 1
    if s == t:      # 목표치에 도달하면
        for j in range(k):
            if bit[j]:  # A[i]가 포함된 경우
                s += A[j]
                print(A[j], end=' ')
        print()

    elif i == k: # 모든 원소를 고려했으나 s!=t
        return
    elif s > t: # 고려한 원소의 합이 t보다 큰 경우
        return
    else:
        # for j in range(1, -1, -1):
        #     bit[i] = j
        #     f(i+1, k, t)
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)

N = 10

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bit = [0] * N     # bit[i]는 A[i]가 부분집합에 포함되는지 표시

cnt = 0
f(0, N, 0, 10)  #처음, 끝, 합의 초깃값, 문자의 갯수

print('cnt : ', cnt)    # 전부 확인하는 경우의 수