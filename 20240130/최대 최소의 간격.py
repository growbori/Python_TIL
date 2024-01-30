# 가장 큰 수는 어디에 있을까
N = int(input())

max_idx = 0 # 첫 번째 원소를 가장 큰 수의 위치로 가정
min_idx = 0
for n in range(1, N+1):
    a = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, a): # 1~a 사이의 범위 동안

        # if arr[max_idx] < arr[i]: #arr[i] 가 더 크면
        #     max_idx =  i # 최댓값의 위치를 i로 변경
        if arr[max_idx] <= arr[i]: # 최댓값이 여러개인 경우 가장 오른쪽
            max_idx = i # 최댓값의 위치를 i로 변경

        if arr[min_idx] > arr[i]: # i 번째 값이 min_idx 번째 값 보다 작으면
            min_idx = i # i 번째 인덱스가 최솟값이다.

    print(f'#{n} {abs(max_idx-min_idx)}') # (max_idx - min_idx) 값이 음수가 나올수 있으므로 abs 를 사용해 절댓값 처리 해준다.


