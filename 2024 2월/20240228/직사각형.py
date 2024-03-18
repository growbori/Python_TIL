'''
두 직사각형이 겹치는 부분이 직사각형인지, 선분인지, 점인지 아니면 전혀 없는지를 판별해서 코드를 작성해야 한다.
2개씩 총 20개의 데이터가 주어짐
a, b, c, d는 직사각형을 이루는 좌표
색칠하기 해서 합이 2인 곳이 있으면 -> 직사각형 1
꼭짓점이 있다. -> a1, a2, c1, c2 중 같은 값이 있다
선분이 있다. -> 하나의 값이 같고 나머지 값은  -> 경우의 수 너무 많으니 else에 넣기
떨어져 있다. -> 범위 안에 숫자가 하나도 없다.
색칠하기!!!!
'''

T = int(input())
for tc in range(T):
    N_array = [list(map(int,input().split())) for i in range(2)]
    N_array.sort()
    A = [[0]* 1001 for _ in range(1001)]
    # print(N_array)
    a = N_array[0][0]
    b = N_array[0][1]
    c = N_array[0][2]
    d = N_array[0][3]

    e = N_array[1][0]
    f = N_array[1][1]
    g = N_array[1][2]
    h = N_array[1][3]

    for i in range(a, c+1):
        for j in range(b, d+1):
            A[i][j] += 1

    for i in range(e, g+1):
        for j in range(f, h+1):
            A[i][j] += 1

    h = 0
    w = 0
    # 색칠한 데이터를 바탕으로 2로 이루어진 직사각형의 가로 세로 구하기
    for row in A:
        if 2 in row:
            h += 1  # 세로
            w = row.count(2)    # 가로

    if h == 1 and w == 1:
        answer = 3

    elif h == 1 or w == 1:
        answer = 2

    elif h > 1 and w > 1:
        answer = 1

    else:
        answer = 4

    print(f'#{tc+1} {answer}')







