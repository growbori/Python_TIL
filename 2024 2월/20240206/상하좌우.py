n = int(input())

arrs = input().split()

x = 1
y = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = [ 'L', 'R', 'U', 'D']

for arr in arrs:
    for i in range(len(move_types)):
        if arr == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

x, y = nx, ny

print(x, y)
'''
5
R R R U D D
'''