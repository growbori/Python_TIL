for tc in range(1, 11):
    # 테이블의 가로와 세로 길이
    N = int(input())
    # 테이블 위의 배열을 저장할 리스트 table
    table = [list(map(int, input().split())) for _ in range(N)]
    # 교착 지점을 셀 변수 cnt
    cnt = 0

    # 열을 하나씩 분석
    for j in range(N):
        magnet = []
        for i in range(N):
            # N 극과 S극을 모두 magnet에 append()
            if table[i][j] == 1 or table[i][j] == 2:
                magnet.append(table[i][j])

        # 뽑아둔 S극과 N극을 하나씩 순회하며 뒤에서 부터 하나씩 뺀다
        # 만약 이전에 뺀게 2 이고 그 다음에 뺀게 1이면 count를 1씩 올려준다.
        previous = 0
        while magnet:
            now = magnet.pop()
            if previous == 2 and now == 1:
                cnt += 1
            previous = now

    print(f'#{tc} {cnt}')
