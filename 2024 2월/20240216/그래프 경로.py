'''
V개 이내의 노드를 E 개의 간선으로 연결할 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
'''

def bfs(i):
    stack = []
    while True:
        for w in adjl[i]:
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
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
    S, G = map(int, input().split())
    bfs(S)
    print(visited[G])