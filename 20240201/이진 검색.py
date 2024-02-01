def binary_search(arr, N, key): # arr 구하고자 하는 배열, N 구하고자 하는 범위 key 구하고자 하는 값
    start = 0 # 구간 초기화
    end = N-1

    while start <= end: # 검색 구간이 유효하면 반복
        middle = (start + end) // 2 # 중앙 원소 인덱스
        if arr[middle] == key: # 검색 성공
            return middle
        elif arr[middle] > key:# 중앙값이 키보다 크면
            end = middle - 1
        else: # 키보다 작으면
            start = middle + 1
    return -1  # 검색 실패

