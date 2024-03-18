def selectionSort(a, N):
    for i in range(N-1): # 주어진 구간의 시작
        minIdx = i  # 맨 앞 원소를 최솟값 위치로 가정
        for j in range(i+1, N): # 실제 최솟값 위치 검색
            if a[minIdx] > a[j]: # 주어진 공간에서 최솟값 구함
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i] # 서로 교환