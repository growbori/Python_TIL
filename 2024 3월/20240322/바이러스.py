def dfs(c):
    global ans_bfs
    ans_bfs += 1
    visited[c] = 1
    for n in adjl[c]:
        if not visited[n]:
            dfs(n)


N = int(input())
M = int(input())
adjl = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adjl[s].append(e)
    adjl[e].append(s)
ans_bfs = 0
visited = [0] * (N+1)
dfs(1)
print(ans_bfs-1)