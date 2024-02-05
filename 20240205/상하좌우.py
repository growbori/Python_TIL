n = int(input())

arrs = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1] # 세로축
dy = [-1, 1, 0, 0] # 가로축
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for arr in arrs:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if arr == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny > 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

'''
5
R R R U D D
'''
