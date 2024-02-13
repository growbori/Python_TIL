t = int(input())
 
for test_case in range(1, t + 1):
    n = int(input())
    maze_map = [list(map(int, input())) for _ in range(n)]
    stack = []
    visited = [[0] * n for _ in range(n)]
    start_x, start_y, end_x, end_y = 0, 0, 0, 0
     
    for i in range(n):
        for j in range(n):
            if maze_map[i][j] == 2:
                start_x , start_y = i, j
                stack.append([start_x, start_y])
            if maze_map[i][j] == 3:
                end_x, end_y = i, j
 
    while stack:
        x, y = stack.pop()
        for dir in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dir[0], y + dir[1]
            if nx == end_x and ny == end_y:
                visited[nx][ny] = 1
                break
            if 0 <= nx < n and 0 <= ny < n:
                if maze_map[nx][ny] == 0 and visited[nx][ny] == 0:
                    stack.append([nx, ny])
                    visited[nx][ny] = True
                else:
                    continue
 
    if visited[end_x][end_y] == 1:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')