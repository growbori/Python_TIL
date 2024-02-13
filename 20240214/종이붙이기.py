def paper():
    for i in range(2, N+1):
        count[i] = (count[i-1] + 2*count[i-2])
    return count[i]

T = int(input())

for tc in range(T):
    N = int(input())
    N = N // 10
    count = [0] * (N+1)
    count[0] = 1
    count[1] = 1
    print(f'#{tc+1} {paper()}')