'''
N 개의 정수가 들어있는 배열에서 이웃한 M 개의 합
합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    answer_list = []     # 합들을 정렬할 리스트 만들기
    for j in range(N-M+1):
        sum = 0     # 합의 값 초기화
        for k in range(j, j+ M):
            sum += arr[k]   # M 개씩 합한 값을 sum에 더하기
        answer_list.append(sum)      # sum 값을 answer에 append 하기
        answer_list.sort()
        answer = answer_list[-1] - answer_list[0]
    print(answer)
