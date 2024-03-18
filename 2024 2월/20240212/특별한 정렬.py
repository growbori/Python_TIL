T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    arr.sort()
    while arr:

        new_arr.append(arr[-1])
        new_arr.append(arr[0])

        arr.pop()
        arr.pop(0)
    print(*new_arr[:10])