#개구리 점프
#규칙 1. 개구리가 점프를 시작하는 위치는 항상 제일 왼쪽(시작시에 밟고 있는 연잎의 숫자는 결과에 더하지 않음)
#규칙 2. 연잎의 숫자가 양수인 경우 앞(오른쪽)으로 점프, 음수인 경우 뒤(왼쪽)로 점프
#규칙 3. 한번 뒤로 갔다가 다시 앞으로 뛸 경우에는 직전에 뒤로 간 칸만큼 더 앞으로 점프
#단, 연속으로 뒤로 간 경우 마지막 뒤로 간 거리만큼만 앞으로 간다.
T = int(input()) #테스트케이스 개수 입력
for tc in range(1, T+1):
    N, K = map(int, input().split()) #N은 연잎의 개수, K는 점프 횟수
    N_list = list(map(int, input().split())) #각 연잎에 적혀있는 숫자 리스트
    pos = 0 #개구리의 위치
    plus_distance = 0 #개구리가 추가로 점프해야 할 거리
    score = 0 #개구리가 밟은 연잎의 모든 숫자의 합
    jump_count = 0 #개구리의 점프 횟수
    while True:
        distance = N_list[pos] #개구리가 이동해야 할 거리
        #연잎에 적혀있는 숫자가 양수일 경우
        if distance > 0:
            pos = pos + distance + plus_distance #개구리 위치 이동
            #만약 위치가 연잎을 벗어난 경우 while문 탈출
            if not 0 <= pos < N:
                break
            jump_count += 1 #점프 횟수 1회 추가
            score += N_list[pos] #현 위치에 적힌 숫자만큼 더해줌
            plus_distance = 0 #다음에 추가 이동할 거리는 0으로 초기화 해줌 (양수니까)
        #연잎에 적힌 숫자가 음수일 경우
        else:
            pos = pos + distance#연잎에 적힌 숫자만큼 위치 이동
            # 만약 위치가 연잎을 벗어난 경우 while문에서 탈출
            if not 0 <= pos < N:
                break
            jump_count += 1  # 점프 횟수 1회 추가
            score += N_list[pos] #현 위치에 적힌 숫자만큼 더해줌
            #뒤로 뛰었으므로 다음에 앞으로 뛸 경우 추가로 뛰어야 할 거리를 -distance로 초기화해 준다.
            plus_distance = -distance
        #개구리가K번 점프할 경우, while문 탈출
        if jump_count == K:
            break
    #각 테스트케이스 별 개구리가 밟은 연잎의 모든 숫자의 합을 출력한다.
    print(f'#{tc} {score}')