di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input().split() )) for _ in range(N)]
total = 0

for i in range(N):
    for j in range(N)