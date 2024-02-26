'''
시작점 갱신 필요

'''
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = []
    # 탐색 시작
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_num = 0 # 최대 숫자 초기화
            # M의 범위 안에서 숫자 검색
            for x in range(M):
                for y in range(M):
                    if max_num < arr[x][y]:     # 만약 arr[x][y]에 있는 값이 최댓값 보다 작다면
                        max_num = arr[x][y]     # 최댓값을 갱신해준다.
                        x = i
                        y = j
            # 시작점을 갱신한다. -> 실패
            if max_num == arr[i][j]:    # 최댓값이 시작값과 같다면
                max_sum.append(max_num) # 조건에 맞는 값들을 max_sum 에 append 한다.
                break
    print(f'#{tc+1} {sum(max_sum)}')