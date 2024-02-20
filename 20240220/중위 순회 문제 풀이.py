'''
in-order 형식으로 순회하며 노드를 특정 단어로 변경
중위 순회  (in-order) 형식으로 순회했을 때 나오는 단어 출력
트리가 갖는 정점의 총 수 N
정점 정보 ( 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식)
루트의 정점번호 항상 1
'''

def in_order(T, N):
    if T <= N:      # 존재하는 노드면
        in_order(T*2, N)        # 왼쪽 자식 방문
        print(tree[T], end = '')        # 부모 노드 처리
        in_order(T*2+1, N)      # 오른쪽 자식 방문
T = 10
for tc in range(1, T):
    N = int(input())
    tree = [0]*(N+1)        # N번 까지 있고, 비어있는 완전 이진 트리

    for _ in range(N):
        node = list(input().split())        # int(node[0]) node 번호, node[1] 저장할 글자
        tree[int(node[0])] = node[1]
    print(f'#{tc}', end = ' ')
    in_order(1, N)
    print()