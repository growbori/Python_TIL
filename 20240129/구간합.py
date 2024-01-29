n = int(input())
front = 0
max_sum = 0
min_sum = 10000
summ = 0
for i in range(1, n+1):
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))

    sumList = []

    # N개의 정수, 구간 M개
    for i in range(a - b + 1):  # 첫번째 수 마지막 위치 a-b+1
        newSum = 0
        for k in range(i, i + b):  # i부터 b번째 수까지
            newSum += arr[k]  # Sum에 할당해서 순회하며 각 구간 합 구함
        sumList.append(newSum)  # 리스트 만들어서 구간 합한 각 결과값 append - sumList 완성

    sumList.sort()
    result = sumList[-1] - sumList[0]
    print(f'#{n} {result}')
