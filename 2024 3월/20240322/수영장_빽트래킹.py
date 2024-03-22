def f(i, s):    # i월까지 비용을 계산하는 함수
    global min_v
    global cnt
    cnt += 1
    if i > 12:
        if min_v > s:
            min_v = s
    elif s >= min_v:     # 최소값보다 값이 크면 돌 필요 없음!
        return
    else:
        f(i+1, s+min(days[i] * day, month))    # i 월만 결제
        f(i+3, s+month3)    # i 월부터 3개월 분 결제

T = int(input())
for tc in range(T):
    day, month, month3, year = map(int, input().split())

    days = [0] + list(map(int,input().split()))   # i 월별 이용일 수 days[i]

    min_v = year    # 1년치를 한번에 결제하는 비용
    cnt = 0     # 재귀호출 횟수
    f(1, 0)
    print(f'#{tc+1} {min_v}')
    # print(f'#{tc+1} {min_v} {cnt}')