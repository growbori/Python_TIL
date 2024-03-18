'''
최소 색칠을 통해 국기 만들기!
몇 줄을 칠할지? -> 몇 칸을 칠할지 -> 최솟값
N줄을 조합? 최소 1이 들어가게!
첫줄은 무조건! 화이트를 제외한 나머지 칸의 수 구하기!
두번째 줄  제일 많이 칠해져 있는 색 구하기 w이면 한칸 더! 아니면 B로 변경!
세번째줄 제일 많이 칠해져 있는 색 구하기  B이면 한칸 더 아니면 R!
앞의 줄이 R이면 나머지 모두 R, 아니면 위 과정 반복
'''

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]

    min_cnt = N* M # 아무리 많아봤자 전체를 뒤집는 경우보다 많을 수 없음
    for i in range(N-2):  # W영역의 마지막 행
        for j in range(N-1):    # B영역의 마지막 행
            cnt = 0     # 칠하는 수
            for x in range(N):
                for y in range(M):
                    if x <= i and arr[x][y] != 'W': # W 영역이 N-2까지 오는 모든 경우의 수
                        cnt += 1
                    elif i < x <= j and arr[x][y] != 'B':   # B 영역이 위에서 구한 i보다는 크고 N-1까지 오는 모든 경우의 수
                        cnt += 1
                    elif j < x and arr[x][y] != 'R':    # j 이상인 모든 범위에서의 경우의 수
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt

    print(f'#{tc+1} {min_cnt}')

