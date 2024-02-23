n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    sumList = []

    # N개의 정수, 구간 M개
    for j in range(a - b + 1):  # 첫번째 수부터 마지막 위치 a-b+1까지 범위에서
        newSum = 0 # b개씩 묶기 위한 초기합 0으로 세팅
        for k in range(j, j + b):  # j부터 b번째 수까지(범위 b)로 해서 범위 내에서 구간 별로 묶음
            newSum += arr[k]  # newSum에 할당해서 순회하며 각 구간 합 구함
        sumList.append(newSum)  # newSum으로 구간 합 나타내고 구해진 값들을 sumList에 append함

    sumList.sort() # sumList에 나타난 구간합들을 오름차순으로 정렬
    result = sumList[-1] - sumList[0] # 제일 적은 구간 합과 제일 큰 구간 합 사이의 값 차를 구함
    print(f'#{j} {result}')
