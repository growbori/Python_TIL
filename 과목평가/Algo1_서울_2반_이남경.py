'''
보너스 게임 점수는 어떤 칸을 맞추면 그 칸의 상하좌우 각 방향으로 두 칸씩 8칸,
총 9 칸의 점수가 보너스 점수가 없다.
상하좌우 중 일부 칸이 없는 경우, 존재하는 칸의 점수만 비교한다.
칸은 N*N 구조로 되어있다.
'''

T = int(input())
for tc in range(T):
    N = int(input())    # 칸수 정보 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 과녁 판 점수 데이터 입력 받기

    dx = [0, 1, 0, -1]      # 상하좌우 칸의 정보들을 입력받기 위한 델타 정보
    dy = [1, 0, -1, 0]
    max_count = 0   # 최댓값 초기화
    for i in range(N):      # i 번째 요소 전부 순회
        for j in range(N):  # j 번째 요소 전부 순회
            count = arr[i][j]   # count  초기값 생성, 과녁에서 맞추고자 하는 값의 점수
            for p in range(1, 3):   # 상하좌우로 2칸씩 점수를 더 얻으므로 p에 1~3 사이 값을 대입
                for k in range(4):  # 델타가 이동하는 4방향 받기
                    nx = i + dx[k] * p  # 상하좌우로 더 구해지는 값들
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:     # nx와 ny 값이 과녁을 벗어나지 않는 조건!
                        count += arr[nx][ny]    # 전체 점수 값들을 더해준다.

            if max_count < count:   # 측정된 점수가 기존의 max_count 값 보다 크면
                max_count = count   # max_count 값이 갱신된다.
    print(f'#{tc+1} {max_count}')