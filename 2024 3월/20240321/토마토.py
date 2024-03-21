'''
보관 후 하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받게 된다.
토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못한다.
철수는 창고에 보관된 토마토들이 몇 일이 지나면 익게 되는지 최소 일수를 알고 싶다.
며칠이 지나면 토마토들이 모두 익는지, 최소 일수를 구하는 프로그램을 작성하라
토마토가 모두 익지 못하는 상황이면 -1을 출력한다.
'''
from collections import deque
def bfs(N, M):
    last = 0    # 마지막 토마토가 익는 순서
    q = deque()     # 큐 생성  → 그냥  q.append(), q.pop()을 쓰면 시간 초과 나옴
    visited = [[0] * M for _ in range(N)]
    cnt1 = 0    # 익은 토마토 개수
    cnt2 = 0    # 빈칸 수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
                visited[i][j] = 1   # 시작점 visited 표시
                cnt1 += 1

            if arr[i][j] == -1: # 토마토가 들어있지 않은 칸
                cnt2 += 1
    if cnt1 + cnt2 == N * M:        # 익은 토마토 수 +빈칸 == 전체 격자, 전체 탐색 완료하면
        return 0    # 다 익은 상태로 리턴
    while q:
        i, j = q.popleft()  # queue!
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):   # 4방향 탐색
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0 and visited[ni][nj] == 0: # 아직 방문하지 않았으면
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1    # 칸에 숫자 1을 더해줌
                last = visited[ni][nj]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                return -1   # 전부 익히는데 실패한 경우 -1 출력

    return last -1      # 마지막으로 익는데 걸리는 시간


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs(N, M))
