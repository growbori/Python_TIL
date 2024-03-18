T = int(input())

for tc in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    arr.sort()

    print(f'#{tc+1}', *arr)