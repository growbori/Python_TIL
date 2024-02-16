'''
10*10 격자에 빨간색과 파란색을 칠하려고 한다.
N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후
보라색이 된 칸 수를 구하는 프로그램을 구하시오
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    book = [[0] * 10 for _ in range(10)]

    for i in range(N):
        c1, a1, c2, a2, t = arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]

        for j in range(c1, c2+1):
            for k in range(a1, a2+1):
                book[j][k] += t

    count = 0
    for i in range(10):
        for j in range(10):
            if book[i][j] >= 3:
                count += 1

    print(count)