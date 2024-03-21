password={
    '0, 0, 0, 1, 1, 0, 1':0,
    '0, 0, 1, 1, 0, 0, 1':1,
    '0, 0, 1, 0, 0, 1, 1':2,
    '0, 1, 1, 1, 1, 0, 1':3,
    '0, 1, 0, 0, 0, 1, 1':4,
    '0, 1, 1, 0, 0, 0, 1':5,
    '0, 1, 0, 1, 1, 1, 1':6,
    '0, 1, 1, 1, 0, 1, 1':7,
    '0, 1, 1, 0, 1, 1, 1':8,
    '0, 0, 0, 1, 0, 1, 1':9
}

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    number = []
    # 1 탐색해서 56자리씩 표시하기
    for i in range(N):
        for j in range(M-1, -1, -1):    # 뒤에서 부터 탐색
            if arr[i][j] == 1:
                number.append(arr[i][j-55:j+1])   # 56자리씩 자르기
                break   # 탐색 끝나면 탈출
    # print(number[0])    # 똑같은게 계속 반복되므로 첫번째 요소만 출력
    # 7 자리 수로 자르기
    bit = []
    for i in range(8):
        bit.append(number[0][7*i:7*(i+1)])
    # print(bit)

    nums = []
    # 딕셔너리에서 찾아 숫자로 변환
    for i in range(8):
        if bit[i] == [0, 0, 0, 1, 1, 0, 1]:
            nums.append(password['0, 0, 0, 1, 1, 0, 1'])    #0
        elif bit[i] == [0, 0, 1, 1, 0, 0, 1]:
            nums.append(password['0, 0, 1, 1, 0, 0, 1'])    #1
        elif bit[i] == [0, 0, 1, 0, 0, 1, 1]:
            nums.append(password['0, 0, 1, 0, 0, 1, 1'])    #2
        elif bit[i] == [0, 1, 1, 1, 1, 0, 1]:
            nums.append(password['0, 1, 1, 1, 1, 0, 1'])    #3
        elif bit[i] == [0, 1, 0, 0, 0, 1, 1]:
            nums.append(password['0, 1, 0, 0, 0, 1, 1'])    #4
        elif bit[i] == [0, 1, 1, 0, 0, 0, 1]:
            nums.append(password['0, 1, 1, 0, 0, 0, 1'])    #5
        elif bit[i] == [0, 1, 0, 1, 1, 1, 1]:
            nums.append(password['0, 1, 0, 1, 1, 1, 1'])    #6
        elif bit[i] == [0, 1, 1, 1, 0, 1, 1]:
            nums.append(password['0, 1, 1, 1, 0, 1, 1'])    #7
        elif bit[i] == [0, 1, 1, 0, 1, 1, 1]:
            nums.append(password['0, 1, 1, 0, 1, 1, 1'])    #8
        elif bit[i] == [0, 0, 0, 1, 0, 1, 1]:
            nums.append(password['0, 0, 0, 1, 0, 1, 1'])    #9
    # print(nums)
    # 결과 값이 10의 배수인지 확인
    odd = 0
    mod = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            odd += nums[i]
        else:
            mod += nums[i]

    total = odd*3 + mod
    answer = 0
    if total % 10 == 0:
        answer = sum(nums)
    else:
        answer = 0

    print(f'#{tc+1} {answer}')
