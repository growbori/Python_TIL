T = int(input())
for tc in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 400

    for i in range(N):
        if room[i][0] < room[i][1]:
            for j in range((room[i][0]-1)//2, (room[i][1]-1)//2+1):
                corridor[j] += 1

        else:
            for j in range((room[i][1]-1)//2, (room[i][0]-1)//2+1):
                corridor[j] += 1

    print(f'#{tc+1} {max(corridor)}')