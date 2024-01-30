'''

최대값이 들어있는 index를 찾는게 key point!

큰 index를 먼저 찾고 그 index가 몇장인지 세기

'''

T = int(input())

for t in range(T):
    N = int(input())
    arr = int(input())
    amount = [0] * 10 # 0~9 
    max_count = 0
    for i in range(N):
        amount[arr % 10] += 1
        arr //= 10

    for amo in amount:
        if amo >= max_count:
            max_count = amo
    
    max_num = amount[0]
    max_index = 1
    
    for j in range(10):
        if amount[j] >= max_num:
            max_num = amount[j]
            max_index = j
    
    print(f'#{t} {max_index} {max_count}')
