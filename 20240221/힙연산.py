## 힙 연산 - 삽입 실습 ##


# 최대힙
def enq(n):
    global last
    last += 1       # 마지막 노드 추가(완전이진트리 유지) ( 삽입할 자리 확장 )
    h[last] = n     # 마지막 노드에 데이터 삽입
    # 부모>자식 조건 만족하도록 관리해야함
    # 부모, 자식 비교를 위해
    c = last        # 자식번호 계산
    p = c // 2      # 부모번호 계산
    while p >= 1 and h[p] < h[c]:   # 이런 상황 = 부모가 있는데, 자식보다 작으면
        # 부모가 존재하고  # 최대힙이니까, 이런 상황이면 자리 바꿔
        h[p], h[c] = h[c], h[p]     # 교환
        c = p
        p = c//2

# 지우는 동작
def deq():
    global last
    tmp = h[1]   # 루트의 키값 임시보관
    h[1] = h[last]  # 힙의 루트에는 마지막 값 넣음
    last -= 1       # 마지막 노드를 삭제 - 접근할 인덱스 줄여놓으면 다음번엔 알아서 거기다 입력되니까\
    p = 1           # 새로 옮긴 루트. insert와 다르게 p 값으로 먼저 접근
    c = p * 2
    while c <= last:    # 자식이 있으면
        if c+1 <= last and h[c] < h[c+1]:    # 자식이 있고 오른쪽 자식이 더 크면
                        # 왼쪽 < 오른쪽 자식
            c += 1
        if h[p] < h[c]:
            h[p], h[c] = h[c], h[p]     # 교환
            p = c
            c = p * 2
        else:           # 부모가 더 크면
            break       # 비교 중단
    return tmp      # 보관했던 tmp return


N = 10              # 필요한 노드 수
h = [0] * (N+1)     # 최대힙
last = 0            # 힙의 마지막 노드 번호

enq(2)
enq(5)
enq(3)
enq(6)
enq(4)

while last > 0:
    print(deq())
'''
6
5
4
3
2
'''