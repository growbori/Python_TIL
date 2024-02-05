N, M = map(int, input().split())
count = 0
# N이 M 이상이라면 M으로 계속 나누기
while N >= M:
    if N % M == 0:
        N = N//M
        count += 1
    else:
        N = N - 1
        count += 1

print(count)

'''
25 5
27 3
'''