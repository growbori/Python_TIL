def dfs(i):
    stack = []
    visited[i] = 1
    while True:
        for w in adjl[i] :
            if visited[w] == 0:
                stack.append(i)
                i = w
                visited[i] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                break


T = int(input())

for tc in range(T):
    V, E = map(int,input().split())
    adjl = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
    S, G = map(int, input().split())
    dfs(S)
    print(visited[G])