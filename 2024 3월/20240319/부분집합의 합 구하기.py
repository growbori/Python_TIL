N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1-10까지 자연수 받아오기
path = [0] * N    # 뭘 선택했는지 정보 담기

def dfs(i, k, t): # i개의 원소 중 k개를 선택, num_sum 은 부분집합의 합
    if i == k:  # 모든 원소에 대해 구하면
        num_sum = 0  # 부분집합의 합을 초기화한다.
        for j in range(k):  # k개를 선택하는 모든 경우의 수에서
            if path[j]:    # arr[i]에 해당하는 값이 있는 경우
                num_sum += A[j]  # 부분집합 요소들의 합 구하기
        if num_sum == t:   # 구해진 합이 10과 같으면
            for j in range(k):
                if path[j] : # A[i] 에 해당하는 값이 있는 경우
                    num_sum += A[j]
                    print(A[j], end = ' ')    # 부분집합 출력
            print()

    else:
        for j in range(1, -1, -1):  # 무조건 숫자가 증가하는 방향으로 작성하기 위해
            path[i]= j
            dfs(i+1, k, t)

dfs(0, N, 10)





