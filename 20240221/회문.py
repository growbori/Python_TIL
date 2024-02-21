'''
8 * 8 평면 글자판에 제시된 길이를 가진 회문의 갯수를 구하여라
'''


for tc in range(10):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(8)]
    count = 0
    # 가로 탐색
    for i in range(8):
        for j in range(8-N+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                count += 1
    # 세로 탐색
    for i in range(8-N+1):
        for j in range(8):
            vertical = ''
            for x in range(i, i + T):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                count += 1
    print(count)