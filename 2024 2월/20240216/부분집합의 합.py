'''
1-12 숫자를 원소로 가진 집합
집합 A의 부분집합 중 N 개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 구하기
부분집합이 없는 경우 0 출력
'''
def f(i, k, N, M):
    global cnt

    if i == k:
        part = []
        for j in range(k):
            if bit[j]:
                part.append(A[j])
        if len(part) == N and sum(part) == M:
            cnt += 1

    else:
        bit[i] = 1
        f(i+1, k, N, M)
        bit[i] = 0
        f(i+1, k, N, M)
T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    A = [i for i in range(1, 13)]
    bit = [0] * 12
    cnt = 0
    f(0, 12, N, K)

