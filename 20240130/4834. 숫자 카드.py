'''

최대값이 들어있는 index를 찾는게 key point!

큰 index를 먼저 찾고 그 index가 몇장인지 세기

'''

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = int(input())
    amount = [0] * 10 # 0~9 사이의 숫자들의 갯수를 나타낼 리스트 형태 생성
    max_count = 0 # 가장 큰 수는 0이라고 초기화
    for i in range(N): # 주어진 문자열의 길이 N 범위 안에 있는 수를 찾을 예정
        amount[arr % 10] += 1 # arr 안에 숫자가 몇개 있는지 조사해서 해당 amount 자리수에 1만큼씩 더하기
        arr //= 10
    # print(amount) amount 안에 0~9 사이의 숫자 들이 알맞게 카운트 되었는지 확인
    for amo in amount: # amount 리스트 안에 있는 값들 중
        if amo >= max_count: # 기존에 주어졌던 max_count 보다 큰 값이 주어지면
            max_count = amo # max_count = amo로 갱신된다.
    # print(max_count) # max_count 값이 맞게 나오는지 확인

    max_num = amount[0] # 가장 큰 수를 amount[0]으로 초기값을 주어줌
    max_index = 1 # 가장 큰 index 값을 1로 초기값을 주어줌

    for j in range(10): # 0~9 사이의 범위동안
        if amount[j] >= max_num: # 새로운 amount[j]의 값이 기존이 max_num 보다 크면
            max_num = amount[j] #max_num 은 amount[j] 이고
            max_index = j # 가장 큰 값의 인덱스는 j 이다.

    print(f'#{t} {max_index} {max_count}')
