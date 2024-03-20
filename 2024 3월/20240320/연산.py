def bfs(N, M):
    q = []          # 큐 생성
    q.append(N)     # 시작점 인큐
    visited = [0] * (1000001)   # visited 생성 노드의 개수가 주어지지 않은 경우, 문제에 맞는 크기를 정해야 함
    visited[N] = 1              # 시작점 표시
    while q:                    # 큐에 탐색할 노드가 남아있으면
        t = q.pop(0)    # pop()만 적을 경우 BFS가 됨
        if t == M:
            return visited[t] - 1
        # t에 인접한 w, 방문한 적이 없으면
        if t - 10 > 0 and visited[t-10] == 0:
            # w = t - 10
            q.append(t-10)
            visited[t-10] = visited[t]+1

        if 0 < t -1 and visited[t-1] == 0:
            q.append(t-1)
            visited[t-1] = visited[t] + 1
        if t+1 <= 1000000 and visited[t+1] == 0:
            q.append(t+1)
            visited[t+1] = visited[t] + 1

        if t*2 <= 1000000 and visited[t*2] == 0:
            q.append(t*2)
            visited[t*2] = visited[t] + 1

    return -1 # 디버깅용 옵션

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    print(f'#{tc+1} {bfs(N, M)}')