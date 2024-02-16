'''
N 개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수 이런식으로 큰 수와 작은 수를 번갈아 가면서 정렬한다.
주어진 숫자에 대해 특별한 정렬을 한 결과 10개를 출력하시오
'''
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    num_list = []
    arr.sort()

    while arr:
        a = arr[-1]
        b = arr[0]
        num_list.append(a)
        num_list.append(b)

        arr.pop()
        arr.pop(0)

    print(*num_list[:10])