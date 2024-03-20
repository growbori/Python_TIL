def find_set(x):
    while x != p[x]:    # 자기 자신을 가르키면(p[x] == x) 대표원소
        x = p[x]
    return x

def union(a, b):
    p[find_set(b)] = find_set(a)    # b의 대표원소가 자기 자신 대신 a의 대표원소를 가르키도록 바꿈

def find_set_r(x):
    if x == p[x]:
        return x

    else:
        p[x] = find_set_r(p[x])     # path compression
        return p[x]

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    p = [i for i in range(N+1)]    # 각자 대표 원소 make_set(1) ~ make_set(N) 까지 생성
    for i in range(M):
        a, b = arr[i*2], arr[i*2+1]
        union(a, b)
    cnt = 0
    for i in range(1, N+1):
        if i == p[i]:   # 인덱스랑 내용물이 같으면 (대표원소인 경우)
            cnt += 1    # 대표원소 개수 == 그룹의 수
    print(f'#{tc+1} {cnt}')





