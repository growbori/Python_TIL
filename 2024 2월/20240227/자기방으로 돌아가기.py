# 색칠하기!!

T = int(input())
for tc in range(T):
    N = int(input())

    room = [list(map(int, input().split())) for i in range(N)]
    move = [0] * 400    # 홀짝 구분! 조건 생성!

    for i in range(N):
        if room[i][0] <= room[i][1]:
            for j in range(room[i][0], room[i][1]):
                move[j] += 1
        if room[i][1] < room[i][0]:
            for j in range(room[i][1], room[i][0]):
                move[j] += 1
    for i in range(N-1):
        if ((room[i][1]+1) // 2) == (room[i+1][0]//2):
            move[j] += 1

        if ((room[i][1]+1) // 2) == (room[i+1][1] // 2):
            move[j] += 1

        if ((room[i][0]+1) // 2) == (room[i+1][0]//2):
            move[j] += 1

        if ((room[i][0]+1) // 2) == (room[i+1][1]//2):
            move[j] += 1
    print(move)
    print(f'#{tc+1} {max(move)}')