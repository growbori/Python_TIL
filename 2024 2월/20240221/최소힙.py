# 최소 힙
'''
최대 힙은 부모가 존재하고 부모가 더 작으면 부모 자식을 교환했었다.
최소 힙은 그와 반대로 부모가 존재하고 부모가 더 크면 부모 자식을 교환한다.
이진 최소 힙은 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
부모 노드 값 < 자식 노드의 값을 유지한다. 조건이 맞지 않을 경우 맞을때까지 부모 노드와 값을 바꾼다.
노드 번호는 루트가 1번 왼쪽에서 오른쪽, 더이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.
'''

def enq(n):
    global last
    last += 1           # 마지막 노드를 추가 (완전 이진 트리 유지)
    h[last] = n         # 마지막 노드에 데이터 삽입
    c = last            # 부모 > 자식 비교를 위해
    p = c // 2          # 부모 번호 계산
    while p >= 1 and h[p] > h[c]:       # 부모가 존재하고 더 크면 앞에 있는게 부모, 뒤에 있는게 자식
        h[p], h[c] = h[c], h[p]         # 부모 자식 교환
        c = p
        p = c // 2


T = int(input())
for tc in range(T):
    N = int(input())    # 노드 수
    num_list = list(map(int, input().split()))
    h = [0] * (N+1)     # 최소 힙
    last = 0            # 힙의 마지막 노드 번호

    for num in num_list:
        enq(num)
    tmp = last // 2
    result = 0
    while tmp:
        result += h[tmp]
        tmp = tmp // 2
    print(f'#{tc+1} {result}')