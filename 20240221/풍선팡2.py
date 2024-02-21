'''
풍선이 M 개씩 N개의 줄에 붙어있고, 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하좌우 추가로 터지면서 꽃가루가 날림
꽃가루의 최대 값 출력하기
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            count = arr[i][j]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    count += arr[nx][ny]

            if max_count < count:
                max_count = count

    print(f'#{tc+1} {max_count}')