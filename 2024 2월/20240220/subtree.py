'''
트리의 일부를 서브 트리라 한다.
이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 구하여라
부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체 루트 노드가 된다.
자식 노드가 0 인 경우에는 노드가 자식이 없는 경우이다.
'''

def pre_order(N):
    global count
    if N:
        count += 1
        pre_order(left[N])
        pre_order(right[N])
    return count

T = int(input())
for tc in range(T):
    E, N = map(int, input().split())        # E 간선의 수, N 서브 트리
    arr = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    par = [0] * (E + 2)

    for i in range(E):
        p, c = arr[i * 2], arr[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    count = 0
    print(f'#{tc+1} {pre_order(N)}')