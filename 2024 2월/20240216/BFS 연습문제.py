'''
다음은 연결되어있는 두개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
모든 정점을 너비우선탐색하여 경로를 출력하시오. 시작 정점은 1로 시작하시오.
V E : V 1~V 번 까지 V 개의 정점. E 개의 간선
E개의 간선 정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, N) :     # 시작정점 s, 노드 개수 N
    q = []  # 큐
    visited = [0] * (N+1)   # visited
    q.append(s)         # 시작점 인큐
    visited[s] = 1      # 시작점 방문표시
    while q:            # 큐가 비워질때까지...(남은 정점이 있으면)
        t = q.pop(0)
        # t에서 할 일....
        print(t)
        for i in adjl[t]:   # t에 인접인 정점
            if visited[i] == 0:     # 방문하지 않은 정점이면
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t]     # 방문표시
    # print(visited)  # 거리 정보를 얻을 수 있음
V, E = map(int, input().split())

arr = list(map(int, input().split()))
# 인접 리스트 형태로 저장
adjl = [[] for _ in range(V+1)] # 0번부터 V 번 까지 배열을 갖는 리스트를 생성
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]   # 2개의 쌍을 읽어내는 방법
    adjl[n1].append(n2)
    adjl[n2].append(n1)     # 무향그래프

bfs(1, V)
