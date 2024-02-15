for tc in range(10):
    N = int(input())
    password = list(map(int, input().split()))

    while password[-1] > 0: # password 마지막 자리에 있는 값이 0이면 계산을 멈추기 때문에 0 보다 클때까지만!
        for j in range(1, 6):   # 1-5까지 범위로 사이클을 돌림
            password.append(password.pop(0)-j)  # password 첫번째 자리 수 에서 j만큼을 뺀 값을 password 마지막에 append
            if password[-1] <= 0:   # 위에서 구한 password 마지막 값이 0보다 작으면
                password[-1] = 0    # 마지막 자리수를 0으로 바꾸고 계산을 멈춘다!
                break


    print(f'#{tc+1}', *password)
