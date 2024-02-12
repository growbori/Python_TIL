for tc in range(1, 11):
    ex = int(input())
    teli = [list(map(int, input().split())) for _ in range(100)]
    result = 0      # 최종 결과값과 연산할때 쓸 변수 생성
    cal1 = 0
    cal2 = 0
    cal3 = 0
    cal4 = 0
    for a in range(100):
        # cal = 0
        for b in range(100):
            cal1 += teli[a][b]   # 행의 합 구하기
            cal2 += teli[b][a]   # 열의 합 구하기
        if cal1 >= result:
            result = cal1   # 합의 최댓값 저장
        cal1 = 0
        if cal2 >= result:
            result = cal2
        cal2 = 0
        cal3 += teli[a][a]       # 대각선 왼쪽 합 구하기
        cal4 += teli[a][99-a]    # 대각선 오른쪽 합 구하기
    if cal3 >= result:
        result = cal3
    cal3 = 0
    if cal4 >= result:
        result = cal4
    cal4 = 0
    print(f'#{tc} {result}')            # for 문 줄여서 다시