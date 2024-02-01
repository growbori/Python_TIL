def selection_sort(a, N):

    for i in range(N-1): # 구간이 시작 i, 2개의 원소가 남을 때 까지
        min_idx = i # 구간의 최솟값 위치 min_idx, 첫 원소를 최소로 가정
        for j in range(i+1, N): # 실제 최솟값을 찾을 인덱스 위치 j
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
    return

N = 5
arr = [1, 3, 2, 5, 4]
print(arr)
selection_sort(arr, N)
print(arr)