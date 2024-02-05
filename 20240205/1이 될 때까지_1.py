N, M = map(int, input().split())
count = 0

while True:
    # (N==M로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (N // M) * M
    result += (N-target)
    N = target
    # N 이 M보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if N < M:
        break
    # M으로 나누기
    result += 1
    N //= M

# 마지막으로 남은 수에 대하여 1씩 빼기
result +=(n-1)
print(result)