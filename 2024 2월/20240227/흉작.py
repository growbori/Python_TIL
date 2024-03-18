T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    sum_potato = arr[0]
    potato_box = []
    max_list = []
    for i in range(1, N):
        if arr[i-1] < arr[i]:   # arr에 있는 값에서 i-1 보다 크면 누적합 구하기
            sum_potato += arr[i]
        else:
            sum_potato = arr[i]
        potato_box.append(sum_potato)   # 누적합 append
    # print(potato_box)

    # 가장 긴 줄기에 달린 고구마의 개수
    # 가장 많은 고구마의 개수를 구하기 위해 조건 사용
    # 두개 이상의 구역에 걸쳐 있어야 하므로 누적합을 비교한 값이 2칸 이상에 적혀있어야 함 (총 3칸)
    for i in range(1, len(potato_box)):
        if potato_box[i-1] < potato_box[i]:
            max_list.append(potato_box[i])
    # print(max_list)
    # print(max_list)


    count = 1   # 기본으로 가지고 있는 개수
    # 긴 줄기의 개수
    # 앞 줄기보다 값이 크고 뒷 줄기보다 값이 작으면 1을 더해준다.
    for i in range(1, len(potato_box)-1):
        if potato_box[i-1] > potato_box[i] and potato_box[i] < potato_box[i+1]:
            count += 1
    # print(count)

    print(f'#{tc+1} {count} {max(max_list)}')