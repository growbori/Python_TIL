'''
상자를 옮겨서 최고점과 최저점의 간격을 줄이는 평탄화 작업을 진행한다.
평탄화를 진행하고 나면 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
상자를 옮기는 횟수에 제한이 있다.
가장 높은 곳에서 가장 낮은 곳으로 상자를 옮기는 작업을 덤프라고 한다.
'''


for tc in range(10):
    dump = int(input())    # 덤프 횟수
    yellow_box = list(map(int, input().split()))

    for _ in range(dump):   # dump 횟수만큼 반복하기
        max_box, min_box = 0, 101
        max_index, min_index = 0, 0

        for i in range(len(yellow_box)):
            if min_box > yellow_box[i]:
                min_box = yellow_box[i] # 최저 높이 찾기
                min_index = i       # 최저 높이의 인덱스 값 찾기

            if max_box < yellow_box[i]:
                max_box = yellow_box[i] # 최고 높이 찾기
                max_index = i         # 최고 높이의 인덱스 값 찾기

        yellow_box[max_index] -= 1  # 최고점에서 1 빼기
        yellow_box[min_index] += 1  # 최고점에서 1 더하기
    # 작업이 끝난 뒤
    max_h = 0
    min_h = 101
    for box in yellow_box:
        if max_h < box:
            max_h = box
        if min_h > box:
            min_h = box
    print(f'#{tc+1} {(max_h - min_h)}')



