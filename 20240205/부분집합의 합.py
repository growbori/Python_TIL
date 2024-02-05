T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for t in range(1, T+1): # 입력받은 T 만큼 테스트 케이스 진행
    N, K = map(int, input().split()) # N = 부분집합 중 N개의 원소, K = 원소의 합
    result = 0 # N, K 조건을 모두 만족하는 케이스의 합합
    for i in range(1 << len(A)): # 2 ^ (len(A) 만큼 개수를 구한 전체 부분집합의 개수 중에서
        num_list = [] # 부분집합 중 N, K 조건을 모두 만족하는 값 들을 더할 빈 리스트 생성
        for j in range(len(A)): # A 의 인덱스 범위 (0 ~ 11)
            if i & (1 << j): # 만약 i 의 j번째 비트가 1인 경우 (ex.3인 경우 100)
                num_list.append(A[j]) # A의 j 번째 인덱스 값을 numlist에 append 한다.
        if len(num_list) == N and sum(num_list) == K: # 위에서 구한 num_list의 길이가 N 이고, num_list 의 합이 K 이면
            result += 1 # 결괏값에 1을 더해준다.
    print(f'#{t} {result}')

