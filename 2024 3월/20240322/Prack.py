def dfs(c):
    ans_dfs.append(c)
    visited[c] = 1

    for n in adjl[c]:
        if not visited[n]:
            dfs(n)
def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    visited[s] = 1
    while q:
        c = q.pop(0)
        for n in adjl[c]:
            if not visited[n]:
                q.append(n)
                ans_bfs.append(n)
                visited[n] = 1


N, M, V = map(int, input().split())
adjl = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adjl[s].append(e)
    adjl[e].append(s)
for i in range(N+1):
    adjl[i].sort()

visited = [0] * (N+1)
ans_dfs = []
dfs(V)
print(*ans_dfs)

visited = [0] * (N+1)
ans_bfs = []
bfs(V)
print(*ans_bfs)