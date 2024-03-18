'''
1-12 숫자를 원소로 가진 집합
집합 A의 부분집합 중 N 개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 구하기
부분집합이 없는 경우 0 출력
'''

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for t in range(T):
    N, K = map(int, input().split())
    result = 0
    for i in range(1 << len(A)):
        num_list = []
        for j in range(len(A)):
            if i & (1 << j):
                num_list.append(A[j])
        if len(num_list) == N and sum(num_list) == K:
            result += 1

    print(result)

