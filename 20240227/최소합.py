'''
N * N 적힌 숫자 판에서 오른쪽이나 아래로만 이동할 수 있다.
이동한 칸에 적힌 숫자의 합곅 최소가 되게 움직였다면, 이때의 합계는 얼마인지 출력하시오
level = (N-1)
branch = 2 (아래로 이동, 오른쪽으로 이동)
'''

def min_sum (x, y, sum):
    global result
    if result < sum:    # 가지치기
        return

    if x == N -1 and y == N-1:  # 도착지에 도착했을 때
        if result > sum:    # 최솟값 구하기
            result = sum
        return

    for dx, dy in [[1, 0], [0, 1]]:     # 아래 혹은 위로만 이동
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N:
            min_sum(nx, ny, sum + arr[nx][ny])  # 이전 칸의 합계 값에 현재 칸의 값 더하기

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 100000

    min_sum(0, 0, arr[0][0])    # sum 시작값 = 위치의 초기값(0, 0)
    print(f'#{tc+1} {result}')