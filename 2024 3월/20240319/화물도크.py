'''
A 도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하시오
작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시되어 있음
앞 작업의 종료와 동시에 다음 작업을 시작할 수 있음
'''

T = int(input())
for tc in range(T):
    N = int(input())
    time_list = []
    for _ in range(N):
        s, e = map(int, input().split())
        time_list.append((s, e))
        time_list.sort(key=lambda x:x[1])   # 오른쪽 값을 기준으로 정렬, 왼쪽값을 기준으로 정렬하고 싶을 경우에는 x[0] 대입
    # print(time_list)

    fi = time_list[0][1]       #첫번째 종료 지점 (무조건 하나를 배치한다)
    count = 1

    for i in range(1, N):
        if time_list[i][0] >= fi:   # 다음 시작점이 이전 종료지점보다 크면
            fi = time_list[i][1]    # 종료 지점을 갱신하고
            count += 1      # 하나를 더해준다.

    print(f'#{tc+1} {count}')