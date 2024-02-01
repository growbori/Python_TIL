T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split())) # 입력 받을 때 리스트 형태로 입력받기
    for i in range(N-1): # 구간이 시작 i, 2개의 원소가 남을 때 까지
        min_idx = i # 구간의 최솟값 위치 min_idx, 첫 원소를 최소로 가정
        for j in range(i+1, N): # 실제 최솟값을 찾을 인덱스 위치 j
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    print(f'#{tc+1}', *arr) # 결과 파일이 리스트 형태로 나온다면 출력하고자 하는 arr 앞에 *를 붙여서 unpack 하면 됨!
