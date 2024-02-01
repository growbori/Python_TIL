t = int(input())

for test_case in range(1, t + 1):
    n = int(input())
    num_list = [[0] * n for _ in range(n)]

    # 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = 0 # x방향 초기값
    y = 0 # y 방향 초기값
    i = 0 # 인덱스에 활용할 초기값
    count = 1 # 123456789 처럼 숫자가 늘어날 초기값
    num_list[0][0] = 1

    while count < n * n:
        nx = x + dx[i]  # i 는 이동할 인덱스 방향 nx는 next x 이동할 위치, x는 현재 위치
        ny = y + dy[i]
        # 이동할 위치가 0보다 작거나 n보다 크거나 (index 여서 = 추가) 이동할 위치의 값이 0이 아니면.
        if nx < 0 or nx >= n or ny < 0 or ny >= n or num_list[nx][ny] != 0: # 혹은 이미 숫자가 적혀있는 칸이면 (0이 아니면)
            i = (i + 1) % 4 # 벽을 넘을때 마다 i의 인덱스 값이 변한다 (i가 4를 넘어가면 5부터는 range를 벗어나는 오류가 발생하기 때문에 (i+1) % 4로 0, 1, 2, 3만 인덱스로 사용)
            nx = x + dx[i]
            ny = y + dy[i]

        x = nx  # 새 위치로 갱신
        y = ny
        count += 1
        num_list[nx][ny] = count

    print(f'#{test_case}')
    for index in range(n):
        print(*num_list[index])  # list 없이 값만 출력해줄 때 * 사용 key, value 뽑고 싶을 때는 **

