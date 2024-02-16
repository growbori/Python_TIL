'''
0 - 9 까지 적힌 카드 N장
가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하는 프로그램
카드 장수가 같을 땐 적힌 숫자가 큰 쪽을 선택!
'''

T = int(input())
for tc in range(T):
    N = int(input())
    card = list(input())
    card_arr = [0] * 10
    for i in range(len(card)):
        card_arr[int(card[i]) % 10] += 1


    card_max = max(card_arr)
    max_index = 1

    for j in range(10):
        if card_arr[j] >= card_max:
            card_max = card_arr[j]
            max_index = j

    print(max_index, card_max)

