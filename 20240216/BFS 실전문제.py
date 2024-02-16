'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''
def bfs(s, N, G) :     # 시작정점 s, 노드 개수 N
    q = []  # 큐 생성
    visited = [0] * (N+1)   # visited 생성
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 인큐 표시
    while q:            # 처리 안된 정점이 남아있으면
        t = q.pop(0)    # 처리할 정점 디큐
        if t == G:
            return  visited[t] - 1    # 시작 점이 1부터 시작하기 때문에 간선 수를 나타내기 위해선 -1을 해줘야 함
        for i in adjl[t]:           # t 의 인접 정점이
            if visited[i]==0:           # 인큐되지 않았으면(처리된 적이 없으면)
                q.append(i)
                visited[i] = visited[t] + 1
    return  0           # G까지 경로가 없는 경우
T = int(input())
for tc in range(T):
    V, E = map(int, input().split())

    # 인접 리스트 형태로 저장
    adjl = [[] for _ in range(V+1)] # 0번부터 V 번 까지 배열을 갖는 리스트를 생성
    for i in range(E):
        n1, n2 = map(int, input().split())   # 2개의 쌍을 읽어내는 방법
        adjl[n1].append(n2)
        adjl[n2].append(n1)     # 무향그래프
    S, G = map(int, input().split())
    print(f'#{tc+1} {bfs(S, V, G)}')    # G 끝까지 가는 목적지
